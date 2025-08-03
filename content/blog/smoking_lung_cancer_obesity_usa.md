---
title: "Smoking, Lung Cancer, and Obesity Rates in the USA"
description: "Exploring the relationships between smoking prevalence, lung cancer incidence, and obesity rates across time periods in the United States."
toc: true
tags:
- data-science
- health
- statistics
- epidemiology
- public-health
categories:
- Data
date: '2025-08-03T10:00:00-04:00'
draft: false
author: hugo-authors
series: ["Statistics"]
featuredImage: images/our_world_in_data_cigs.jpeg
---

The chart above by the World In Data is a striking piece of data visualisation, showing us how lung cancer and cigarette sales are strongly related to each other.

However, given that cigarettes are also an appetite suppressant, I have always wondered what the chart would look like if we include obesity rates. Obesity started becoming a problem more or less when cigarette sales started to drop.

This isn't to imply that one directly caused the other, but it does warrant some investigation. Anyway, I decided to replicate the famous chart and include obesity rates in it.

![image](/images/cigarettes_health_outcomes_usa.png)


The main difficulty plotting this is that obesity rates are really high (up to 40% of the population) whereas lung cancer incidences are far lower (up 70 people per 100000 men, so 0.07%). It would've been tempting to make the lung cancer incidence chart way smaller, but that would've been a bit misleading. Being obese is of course far less bad than dying from lung cancer. 
