---
title: Automating my business
description: Using scripts to automate menial tasks.
toc: true
tags:
- R
- coding
categories:
series: Hacking
date: '2019-08-12T13:11:22+08:00'
featuredImage:
draft: false

---

As a small business owner keeping track of things can be surprisingly difficult: how you spend your money, who owes you money, who you owe money, what are your expenses, margins, operating costs...

If you have multiple revenue streams from multiple platforms, you can quickly reach a point where you ignore basic things, like for example how much you are making exactly. Specially when you are focused on numerous other things as you try to scale your business. I am guilty of having neglected this in the past.

To give the reader some context: I run tourism focused e-commerce websites, such as [ZunZunCar.com](www.zunzuncar.com) and [CubaBackpacker.com](www.cubabackpacker.com).

My process for knowing my numbers was to create a spreadsheet every month, where I exported data from my websites, my property management software, my email and my bank, in order to get an idea of where the business was standing. The problem with this process is that it is boring, took a lot of time and I ended up not doing it as often as I should've and was "flying in the dark" often.

Hence, my goal was to create a set of automatic reports that allowed me see exactly how much money we were making, where the expenses were going, and automate away as much of my work as possible. In particular, I wanted to know:

-   how much we were making in commissions with the transportation business
-   how much we were making in commissions with the accommodation business
-   how much we had to pay suppliers, partners & affiliates

How I built it
--------------

I had already created an AWS instance following [this guide](http://www.louisaslett.com/RStudio_AMI/) when I [automated away some of my emails](http://boazsobrado.com/blog/2018/11/08/a-smart-email-sms-bot-on-aws-using-r/). Now I had to put it to work.

The process would be the following:

1.  Get the data (via API's and/or email)
2.  Process the data
3.  Create reports.
4.  Schedule & email reports
5.  Automate away other repetitive tasks

Getting the data
----------------

Fortunately, almost all of the services I use (bank, Woocommerce and property management software), have either an API or a database which I could access through R using the `httr` or `RMySQL` libraries. Where data is missing I have to either go through my email programmatically to extract the missing data (more on this later) or fire up an `RSelenium` instance to simulate a browser in order to get this data.

For example, I wrote the following function to access all the accommodation bookings I'd gotten on my property management platform:

```

# Function to get data from Beds24 API
getBeds24Data <-function(username = property_mgmt$username,
                         password = property_mgmt$password,
                         datefrom = "2019-01-01",
                         dateto = "2019-12-30"){
  url <- "https://www.beds24.com/api/csv/getbookingscsv"

  response <- httr::POST(url=url, body = list("username" = username,
                                              "password"=password,
                                              datefrom = datefrom,
                                              dateto = dateto))
  beds24Data <- httr::content(response,type='text/csv',col_names=T,col_types=NULL)
  return(beds24Data)
}

```

Luckily most API's were similarly easy to deal with.

However, the Woocommerce bookings were a bit more complicated to get, because all the relevant information (client name, product booked, etc.) was scattered across a wide range of SQL tables that had to be joined together to get all the relevant information.

At this point I also decided to add products to my site programmatically, and I managed to break my website a few times. This is how I discovered that `RMySQL`'s `dbWriteTable()` function ads a column with row-numbers by default, and that that broke the PHP functions which make my website usable. Fortunately, I managed to fix it within a few (panicked) minutes.

Processing the data
-------------------

Now that the data is in R, it must be cleaned and processed in order to create meaningful reports. This can be a tedious task but oddly satisfying task. Anyone who is used to dealing with data can attest to this.

An example: In the case of the data from ZunZunCar.com this involved joining and cleaning 7 different SQL tables in both long and wide formats in order to get the following information:

-   Client name & information
-   Order information (order ID, from where to where, type of service etc.)
-   Extras purchased by clients
-   Affiliate information

### Using email to fill in gaps

I found that a lot of data was missing from the property management system because the iCAL connection between Airbnb and Beds24 did not pass on information on the price of the booking. Airbnb has an API, but it isn't public, so I cannot access it that way.

What ended up doing is creating a function to read my emails using the `gmailR` package, to extract the information from Airbnb's booking confirmation email:

```
# a function to look through emails to find out AIRBNB total payout in USD given that it isn't passed through iCAL connections

getAirbnbPayout <- function(resCode = "HMAKQYK4NQ"){

  gmail_auth(scope= "full",secret_file = "client_id.json")

  searchResults<- messages(paste0("\"Reservation confirmed\""," ",resCode)) %>%
    unlist(.,recursive = FALSE)

  searchResultsDf <- dplyr::bind_rows(searchResults$messages)

  id <- searchResultsDf$id[1]
  #extract message
  resultMessage <- message(id, format = "full")
  resultMessageBody <- body(resultMessage) %>% as.character()

  amount_sent <- str_match(resultMessageBody,"\nTotal \\$(.*?)\\r") %>%
    dplyr::nth(2)

  return(as.numeric(amount_sent))
}

```

Creating reports
----------------

Here I used the `Rmarkdown` to create html documents. Here is an example of an .RMD file that generate an email every month to our affiliates:

```
{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)

library(RMySQL)
library(readr)
library(tibbletime)
library(dplyr)
library(kableExtra)
library(openxlsx)

Dear Affiliate Partner,

For this month from `r monthStart` to `r monthEnd` we've **completed** the following affiliate bookings from your site. These are not all the bookings we received from you, only the ones that we actually executed already.

The rows in red were either cancelled (for example due to cancelled flights) or not fulfilled (e.g. last minute viazul tickets which we couldn't buy).

{r, echo=F, warning=FALSE}

options(knitr.kable.NA = '')

# get last months'
presentBookings <- getZZCBookingsAll(zzc_bookings) %>%
  filter(affiliate == params$affiliateEmail) %>%
  as_tbl_time(transferTime) %>%
  filter_time(monthStart~monthEnd)

# write CSV file
presentBookings %>%
  select('Transfer Time'  = transferTime,
         'Order ID'  = woo_order_id,
         'Type'  = tipo,
         'First Name'  = first_name,
         'Last Name'  = last_name,
         'People'  = people_count,
         'From'  = from,
         'To'  = to,
         'Total Price'  = total_price,
         'Extras'  = extras,
         'Affiliate Fee'  = affiliateCost,
         'Order Status'  = woo_status) %>%
  write_csv(., path = "../Data/affiliate.csv")

futureBookings <- getZZCBookingsAll(zzc_bookings) %>%
  filter(affiliate == params$affiliateEmail) %>%
  as_tbl_time(transferTime) %>%
  filter_time("2019-08"~"2022-12")

presentBookings %>%
  select('Transfer Time'  = transferTime,
         'Order ID'  = woo_order_id,
         'Type'  = tipo,
         'First Name'  = first_name,
         'Last Name'  = last_name,
         'People'  = people_count,
         'From'  = from,
         'To'  = to,
         'Total Price'  = total_price,
         'Extras'  = extras,
         'Affiliate Fee'  = affiliateCost,
         'Order Status'  = woo_status) %>%
  knitr::kable(booktabs = T) %>%
  kable_styling() %>%
  row_spec(which(presentBookings$woo_status %in% c("on-hold","cancelled")), bold = T, color = "white", background = "red")

Our total debt to you for the month of July is `r presentBookings %>% filter(woo_status %in% c("processing","completed")) %>% summarise(sum(affiliateCost)) %>% pull()` USD.

We've registered `r futureBookings %>% summarise(n()) %>% pull()` bookings from you that have yet to be executed, with a total value to you of `r futureBookings %>% summarise(sum(affiliateCost)) %>% pull()` USD.

All the best,
ZZC team

```

Scheduling the emails
---------------------

I created several script with the logic & conditions (e.g. send last minute booking warning email to last minute bookers) to each report as well as their frequency.

For instance, in a script titled `daily.R` contains all transportation bookings we have for the day and the next few days. The essence of it is this:

```
# generate report
rmarkdown::render("zunzunAutomation/Reports/daily_transfers.Rmd")

#craft email using generated html file
daily_transfers <- mime() %>%
  to("email@email.com") %>%
  cc("email@email.com") %>%
  from("email@email.com") %>%
  subject("ZZC- Rutas diarias Report") %>%
  html_body("") %>%
  attach_file("zunzunAutomation/Reports/daily_transfers.html")

# Send email
send_message(daily_transfers)
cat("Daily Transfers message sent ..\n")

```

The `daily.R` script is scheduled to run once a day in the morning using the `cronR` package.

Automating away repetitive tasks
--------------------------------

The same logic of:

1.  Retrieve data
2.  Generate HTML report
3.  Send via email

Is also applied to communication with clients, even in an iterative way using simple `IF THEN` statements.

For example, after our colleagues mark a transport as completed, we send clients an email asking for feedback on a Google Form. If the feedback is good, then we automatically ask them a day later to share it on public sites like TripAdvisor. All of this is automated (we always read our client feedback personally though).

Other than reporting and communication, one can also automate other mundane tasks such as payments. For instance, our bank's API allows us to send funds programmatically, which we could do for all of our affiliates. As of now I haven't implemented this yet, but doing so wouldn't be harder than adding a few lines of code.

Summary
-------

Being able to use APIs and schedule scripts on the cloud is incredibly powerful, and I'm really glad I've gotten to the point of being comfortable enough with R to do it. However, I have noticed that it would be useful to get more comfortable with a more general scripting language, such as Python, because R doesn't always have packages for common API's, whereas more common scripting languages do.
