+++
date = "2016-11-13T15:52:58+02:00"
draft = false
title = "You are wasting your time with spreadsheets"
tags = ["R"]
Categories = ["R","Excel"]
series = "hacking"
+++

<p>This week I had an interesting conversation (as interesting as these conversations can get) about the use of spreadsheets in business. I am still a little bit surprised by how often they are used for things they are not really good for. Now, I don’t want to write about how there are <a href="http://blog.revolutionanalytics.com/2014/10/why-r-is-better-than-excel.html">better alternatives to spreadsheets</a>. Instead, I’d like to illustrate how powerful non-spreadsheet tools are by describing a task I completed this week using R.</p>
<p> I was recently asked to help an NGO aggregate their contact database. It was not a surprise they needed help aggregating it: it came from dozens of different sources, and had thousands of partially duplicated entries. Entries were identifiable by name or by emails, which were the only unique columns.</p>
<p>To give you a better idea, this is what it looked like:</p>
<table>
<thead>
<tr class="header">
<th align="left">source</th>
<th align="left">email</th>
<th align="left">firstName</th>
<th align="left">lastName</th>
<th align="right">details1</th>
<th align="right">details2</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">This</td>
<td align="left"><a href="mailto:wrw@cs.com">wrw@cs.com</a></td>
<td align="left">Bob</td>
<td align="left">ANna</td>
<td align="right">1</td>
<td align="right">5</td>
</tr>
<tr class="even">
<td align="left">That</td>
<td align="left"><a href="mailto:zam@pk.com">zam@pk.com</a></td>
<td align="left">Steve</td>
<td align="left">NA</td>
<td align="right">2</td>
<td align="right">4</td>
</tr>
<tr class="odd">
<td align="left">Other</td>
<td align="left"><a href="mailto:s2@qs.com">s2@qs.com</a></td>
<td align="left">NA</td>
<td align="left">Lacey</td>
<td align="right">3</td>
<td align="right">3</td>
</tr>
<tr class="even">
<td align="left">Other</td>
<td align="left"><a href="mailto:zam@pk.com">zam@pk.com</a></td>
<td align="left">Steve</td>
<td align="left">Lacey</td>
<td align="right">4</td>
<td align="right">2</td>
</tr>
<tr class="odd">
<td align="left">NA</td>
<td align="left"><a href="mailto:zam@pk.com">zam@pk.com</a></td>
<td align="left">Lacey</td>
<td align="left">Steve</td>
<td align="right">5</td>
<td align="right">1</td>
</tr>
</tbody>
</table>
<p>Except that I had several columns with details, many emails and other values were invalid, or missing. In short, it was a big hassle that would have taken days of manual work in spreadsheets to sort out, which was what the client originally tried.</p>
<p>A more sophisticated consultant/banker spreadsheet user would’ve written some extensive for loop with dozens of conditions and incessant F10 pressing and debugging. This probably would’ve worked but would have been a great waste of time, with a lot of places for errors to creep in.</p>
<p>So how did I solve it in R? Almost all of the heavy lifting was done by a single function in the <a href="https://cran.rstudio.com/web/packages/dplyr/vignettes/introduction.html">dplyr</a> package. After some data-preprocessing, the hardest problem was solved by the following lines of code:</p>
<pre class="r"><code>library(stringr)#loading package to deal with strings
library(dplyr)#loading data wrangling package

#first I write a function to give the most common value in a vector
# a concrete example in this case, the first name that happens most commonly under a given email
mstcmn&lt;-function(x){
  x&lt;-names(sort(table(as.character(x)),decreasing=TRUE)[1])
  if (is.null(x)){
    return(NA)
  }
  return(x)
}

#then I write a function to aggregate all other unique strings
aggr&lt;-function(x){
  x&lt;-toString(na.omit(x))
  x&lt;-str_split_fixed(x,&quot;,&quot;,(str_count(x,&quot;,&quot;)+1))
  x&lt;-trim(x)
  x&lt;-unique(as.list(x))
  return(toString(unlist(x)))
}


#and most of the magic happens here: the C++ code under dplyr's hood rapidly and efficienly aggregates the information needed
newdf&lt;-olddf %&gt;% group_by(email) %&gt;% summarise(source = aggr(source),
                                              first  = mstcmn(first_name),
                                              last  = mstcmn(last_name),
                                              details1 = aggr(details1),
                                              details2 = aggr(details2))</code></pre>
<p>This was followed by a few lines of code to capitalise all relevant values, make things pretty. And voila:</p>
<table>
<thead>
<tr class="header">
<th align="left">source</th>
<th align="left">email</th>
<th align="left">firstName</th>
<th align="left">lastName</th>
<th align="left">details1</th>
<th align="left">details2</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">This</td>
<td align="left"><a href="mailto:wrw@cs.com">wrw@cs.com</a></td>
<td align="left">Bob</td>
<td align="left">Anna</td>
<td align="left">1</td>
<td align="left">5</td>
</tr>
<tr class="even">
<td align="left">That, Other</td>
<td align="left"><a href="mailto:zam@pk.com">zam@pk.com</a></td>
<td align="left">Steve</td>
<td align="left">Lacey</td>
<td align="left">2, 4, 5</td>
<td align="left">4, 2, 1</td>
</tr>
<tr class="odd">
<td align="left">Other</td>
<td align="left"><a href="mailto:s2@qs.com">s2@qs.com</a></td>
<td align="left">NA</td>
<td align="left">NA</td>
<td align="left">3</td>
<td align="left">3</td>
</tr>
</tbody>
</table>
<p>I also recreated people’s names based on their emails if their names were missing, as most professional emails in the format: <a href="mailto:firstname.lastname@email.com">firstname.lastname@email.com</a>.</p>
<p>Then I used the <a href="https://cran.r-project.org/web/packages/genderizeR/genderizeR.pdf">genderizeR</a> package to add a column with people's titles: Mr or Ms based on their name.</p>
<p>Try doing this on a spreadsheet. I guess the main argument of this post is: don't use spreadsheets for more than what they are for.</p>
