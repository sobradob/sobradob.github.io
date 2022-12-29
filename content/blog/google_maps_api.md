+++
date = "2015-11-05T11:36:16+01:00"
draft = false
title = "Using Google Maps API: Mol Bubi Competition"
tags = ["R","coding"]
Categories = ["R","Maps"]
series = "Hacking"
+++
A few friends and I are involved in the Budapest public bicycle data science [competition](https://dms.sztaki.hu/bubi/#/app/home). As of right now we are in the top ten, although in all honesty, it hasn't really started yet.
We signed a non-disclosure agreement, so I cannot really share any cool details. What I can share however, is the function I wrote in R to get calculate the distances and duration of bike trips using Google Maps' [API](https://developers.google.com/maps/?hl=en).

```
#distance calucations
#### This script uses RCurl and RJSONIO to download data from Google's API

library(RCurl)
library(RJSONIO)

#define api key as: api<-"YOURAPI"
#the function assumes address input in following dataframe:
#lat1,lng1,lat2,lng2

DistDur <- function(address,time = as.integer(Sys.time()),mode, return.call = "json", sensor = "false") {
  address1<-paste(address[,1],address[,2], sep=" ")
  address2<-paste(address[,3],address[,4], sep=" ")
  root <- "https://maps.googleapis.com/maps/api/directions/"
  u <- paste(root, return.call, "?origin=", address1, "&destination=",address2,"&departure_time=",time,"&mode=",mode,"&key=",api,sep = "")
  for (a in 1:length(u)){
    url<-URLencode(u[a])
    doc <- getURL(url)
    x <- fromJSON(doc,simplify = FALSE)
    dist<-0
    dura<-0
    for (i in 1:length(x$routes[[1]]$legs[[1]]$steps))
    {
      dist<-x$routes[[1]]$legs[[1]]$steps[[i]]$distance$value+dist
      dura<-x$routes[[1]]$legs[[1]]$steps[[i]]$duration$value+dura
    }
    address$dura[a]<-dura
    address$dist[a]<-dist
  }
  return(address)
}
```
The code itself is quite simple, but its my first time using the Google Maps API and I was amazed by how easy it was. This and more can be found on my [Github](www.github.com/sobradob).
