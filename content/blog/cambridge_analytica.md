---
title: My thoughts on Cambridge Analytica
description: On my role in unearthing the Cambridge Analytica scandal and why psychographic advertising does not work.
toc: true
tags:
- advertising
categories:
date: '2020-11-07T13:11:22+08:00'
draft: false
series: Advertising
---

I am writing this to share my conclusions regarding the Cambridge Analytica affair. I have a somewhat unique perspective on the topic for three reasons:

-   My day job consists of measuring the effectiveness of digital advertising.
-   I have first hand experience with the technology and methods that Cambridge Analytica claims to have used.
-   I played a small role in unearthing the Cambridge Analytica scandal.

What Cambridge Analytica supposedly did
---------------------------------------

The New Statesmen's Laurie Clarke puts it in the [following way](https://www.newstatesman.com/science-tech/social-media/2020/10/how-cambridge-analytica-scandal-unravelled):

> CA was alleged to have mined Facebook data from millions of people worldwide. The data was detailed enough for CA to create complex psychographic profiles of its subjects, to deliver pinpointed adverts to them and propel them into new behaviour patterns. The CA whistleblower Christopher Wylie described it as "Steve Bannon's psychological warfare mind-fuck tool".

In the Netflix documentary *The Great Hack* Brittany Kaiser, the former business development executive of Cambridge Analytica says:

> "If we targeted enough persuadable people in the right precincts, then those states would turn red instead of blue... We bombarded them through blogs, websites, articles, videos on every platform you can imagine until they saw the world the way we wanted them to -- until they voted for our candidate."

The implication here being that two of the greates political upsets of the last decade (Brexit & Trump) were due to the advanced persuasion technology that Cambridge Analytica sold to the highest bidder.

My concern is that a lot of people seem to focus on a scary technology called psychographic advertising (also known as psychographic or [personality marketing](https://hbr.org/2018/05/what-marketers-should-know-about-personality-based-marketing)) that purportedly allowed Cambridge Analytica to manipulate people by serving them ads tailored to their individual personality. My argument is that this technology is mostly ineffective in the context of modern digital advertising and is unlikely to have had the influence attributed to it. Moreover, it distracts from the true issues at stake, such as data privacy in the days of "[surveillance capitalism](https://www.theguardian.com/technology/2019/jan/20/shoshana-zuboff-age-of-surveillance-capitalism-google-facebook)".

My role in the story
--------------------

Between 2012 and 2014 I did some work at the Cambridge University Psychometric Centre in as an undergraduate, and I met in person Alex Kogan and a lot of the people who were mentioned in the [books](https://www.michalkosinski.com/clown-show) and [articles](https://www.nytimes.com/2018/03/17/us/politics/cambridge-analytica-trump-campaign.html) that have been written about the whole scandal. While at Cambridge I had access to key parts of the data set that inspired Cambridge Analytica's work.

In 2015 I spent some time at Stanford, where I recruited several well-known brands (who I presume would rather not be named) to test psychographic marketing in a commercial setting. While doing my research on psychographic marketing, I discovered that a little known company called Cambridge Analytica was working with Ted Cruz on psychometric targeting in digital advertising.

I pointed this out to [Dr Michal Kosinski](https://www.michalkosinski.com/), who was familiar with the unethical way in which the Cambridge Analytica had collected its data. Michal then got in touch with a journalist at the Guardian, who produced the [first article](https://www.theguardian.com/us-news/2015/dec/11/senator-ted-cruz-president-campaign-facebook-user-data) in what later became known as the Cambridge Analytica scandal in December 2015.

Eventually I failed to get psychographic advertising to work for commercial purposes in 2015 and moved on to other projects. Since then, I've also spoken to other teams that spent years trying to get a commercially viable personality marketing to work, who also failed. As far as I know, Facebook also ran some tests internally and decided not to proceed with it in early 2015. From this I drew the conclusion was that psychographic marketing doesn't **really** work, particularly not in the way Cambridge Analytica claimed it did. Let me illustrate why by looking at one of the key scientific papers on personality marketing.

What the science says
---------------------

This [paper](https://www.pnas.org/content/114/48/12714/) was written by Sandra Matz and friends. The experiments they describe are clever: studies 1 and 2 show that you can target high individuals who score highly along a certain personality dimension (say, are extroverted), and that these individuals respond better to messages crafted for their end of the dimension than the opposite dimension (e.g. highly extroverted people respond better to high extroversion crafted messages than low extroversion messages). In study 3, they show that a psychologically targeted message towards introverts performed better than the copy used by a company previously.

This study is important in that it demonstrates three things:

-   It is possible to target people online based on their personality
-   It is possible to tailor messages to people online based on their personality, and these messages perform better than those tailored for people with an opposite personality.

What Sandra's paper does not show, is that psychographic advertising performs better than standard methods used in digital advertising. In my experience it does not, and I can explain why.

Personality based advertising is based on a simple five dimensional model of human beings, designed to explain behaviours as diverse as reading books and going to clubs. Facebooks machine learning algorithms create a high dimensional model finely tuned with thousands of data points trying to optimise for very specific outcomes, such as purchasing a MAGA hat. The former is a general descriptive model built using statistical methods of the mid 20th century, with some but overall limited predictive general validity. The latter is a highly specialised machine learning model, with little descriptive power, but lot more accurate at predicting specific behaviours like the purchases of haircuts.

Digital advertising in practice
-------------------------------

Keeping that in mind, which of these two digital approaches do you think will yield better results?

-   Approach A: Summon the best psychologists and copywriters in the world to write copy that will get extroverted people to purchase a brand of deodorant. Target highly extroverted people on Facebook with that copy by advertising to people who have "liked" highly extroverted pages.
-   Approach B: Using Facebook's machine learning algorithms generate a Lookalike audience based on previous purchasers on your site. Target these people with thousands of different types of programmatically generated messages, and focus on the better performing ones.

When I researched this in 2015 I found that Approach B will perform better at all times. In fact, Approach B is more like what Trump [actually did in 2016](https://www.theatlantic.com/technology/archive/2020/04/how-facebooks-ad-technology-helps-trump-win/606403/):

*"During the 2016 election cycle, Trump's team ran 5.9 million ads on Facebook, spending $44 million from June to November alone. Hillary Clinton's campaign ran only 66,000."*

Instead of trying a fancy secret sauce on how to design creatives and how to target them Trump's team just threw everything at the algorithm and stuck with the ads that performed the best. All the psychological theory in the world has limited efficiency compared to the AI powering Facebook's ad optimisations.

So what do I think?
-------------------

In conclusion, it is not that psychographic advertising doesn't work at all. The science behind it is solid, and it is worthy of study. My point is that psychographic advertising afforded Cambridge Analytica little to no advantage at all. Cambridge Analytica was working with more or less the same technology as their competitors. Most of the outlandish claims made by Cambridge Analytica were just branding, and subsequently sensationalism by reporting journalists. These are not just my conclusions by the way, they are also the findings of the [British Information Commissioner's Office](https://ico.org.uk/media/action-weve-taken/2618383/20201002_ico-o-ed-l-rtl-0181_to-julian-knight-mp.pdf) (excellent summary [here](https://twitter.com/nickconfessore/status/1313853996168351747)). The "secret sauce" part of this affair should not distract from the wide scale data harvesting of large tech monopolies and the data privacy issues that arise from it.
