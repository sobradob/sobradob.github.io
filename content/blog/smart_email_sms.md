---
title: Automating SMS & email
description: A smart email & SMS bot on AWS using R.
toc: true
tags:
- R
- coding
categories:
date: '2018-11-08T13:11:22+08:00'
featuredImage:
draft: false
---


I face the following problem: I get a lot of similarly formatted emails that require some sort of action that can in theory be easily automated. For example, I get Woocommerce order notifications that I want to forward selectively to my team via SMS.

It turns out there is no Gmail extension that will help you do that (or at least I didn't find anything like it). A better programmer would alter the php code of the Woocommerce site to interact with the API of a service like [SMSGLOBAL](https://www.smsglobal.com/). I couldn't quite wrap my head around the php code, and it didn't really solve the issue of the other types of emails I get that require relatively automation.

For example, if you get an email from someone asking you a question in Spanish, why would you send them an "out of office" email in English?

In order to solve this I set up a script to monitor my emails using [gmailr](https://cran.r-project.org/web/packages/gmailr/index.html).

This function checks the email to see if I have any recent emails with a particular string:

```
checkEmail <- function(searchString="from: X@example.com [Test]: New Order",minutesThreshold=20){

  searchResults<- messages(searchString) %>%
    unlist(.,recursive = FALSE)

  cat(
    paste0(
      searchResults$resultSizeEstimate," results found for ",searchString,"\n"))

  # extract bookings
  searchResultsDf <- dplyr::bind_rows(searchResults$messages)

  selectid <- vector()

  for(i in 1:nrow(searchResultsDf)){
    # get individual ID
    id <- searchResultsDf$id[i]
    #extract message
    resultMessage <- message(id, format = "full")
    # Get the time received of the message
    timeReceived <- resultMessage$internalDate %>%
      as.numeric() %>%
      `/`(1000) %>%
      as.POSIXct(origin= "1970-01-01")

    cat(paste0("Message received at ",timeReceived,"\n"))

    # if it was a long time ago ignore
    if(
      (timeReceived) < (Sys.time()-minutesThreshold*60)
    ){
      cat("No recent messages found \n")
      break
    }else{
      selectid[i] <- id
    }
  }
  return(selectid)
}

```

And this function drafts an email based on the emails received in the last 20 minutes using [stringr](https://cran.r-project.org/web/packages/stringr/vignettes/stringr.html):

```
function(resultMessage){
  resultMessageBody <- body(resultMessage) %>% as.character()

  name_client <- str_match(resultMessageBody,"order from (.*?):</p>") %>%
    dplyr::nth(2)

  flight_from <- str_match(resultMessageBody,"Flying From \\(write NA if not applicable\\): (.*?)</p>") %>%
    dplyr::nth(2)

  address <- str_match(resultMessageBody, "Address:(.*?)<br>Flight") %>%
    dplyr::nth(2)

  product <- str_match(resultMessageBody,"Transfer from(.*?)\\(#transfers_transfer_511205\\)") %>%
    dplyr::nth(2)

  flight_num <- str_match(resultMessageBody,"Flight Number \\(write NA if Not Applicable\\): (.*?)<br>") %>%
    dplyr::nth(2)

  flight_from <- str_match(resultMessageBody,"Flying From \\(write NA if not applicable\\): (.*?)</p>") %>%
    dplyr::nth(2)

  # construct message

  smsNotifyText <- paste(name_client,product,flight_num, flight_from, address,sep = " ") %>%
    str_replace_all("<br>"," ")

  # send message
  notification_email <- mime(
    To = "test@test.com",
    From = "test@gmail.com",
    Subject = paste("Flight Notification",Sys.time()),
    body = smsNotifyText)
  send_message(notification_email)
  cat("Notification email sent \n")
}

```

I wrapped these functions together in a script and tested it on my laptop. It worked well! Using SMSGLOBAL all I need to do is send the message to a particular email and my team members will recieve it via sms.

Then I set up an R Studio AWS instance using [this amazing guide](http://www.louisaslett.com/RStudio_AMI/).

However, when I first tested my script I ran into authentification issues. I managed to solve it based on googling around and finding this post on [Oauth tokens generated server side](https://support.rstudio.com/hc/en-us/articles/217952868-Generating-OAuth-tokens-from-a-server).

Finally I set up [CronR](https://github.com/bnosac/cronR) to check my emails every fifteen minutes and send out the email.

I am quite pleased at myself about this because:

1.  This is my first script continuously running on the cloud.
2.  It opens the door to a lot of automation of tedious tasks.
