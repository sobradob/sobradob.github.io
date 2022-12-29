+++
date = "2017-05-22T22:22:16-08:00"
draft = false
title = "Bayesian Images"
tags = ["R","Bayes"]
Categories = ["R","Bayes"]
series = "Statistics"

+++

Graphs to accompany my poster presentation.

## The data set

The generated data is plotted below:
![data](/images/explorePlot.png)

## Metropolis Hastings Algorithm
![mhalgo](/images/metropolis_hastings2.gif)

This visual explanation of the Metropolis Hastings algorithm shows the proposal and the true density along with the Metropolis Hastings step. It was inspired and adapted from code by [Balazs Torok](https://www.researchgate.net/profile/Balazs_Toeroek6).

## Diagnostic Plots for Beta 2 via Gibbs Sampler

### Autocorrelation Plot
![acf](/images/acfb2.png)

The autocorrelations are negligable, suggesting good mixing.

### Running Means Plot
![rmp](/images/b2runningmeans.png)

The running means have settled.

### Three chain trace plot
![traceplot](/images/traceb2.png)

All three chains seem to be in the same place.

## Posterior Predictive Checks

![ppcheck](/images/ppCheck.png)

On the left side you can see the two predictive check using the maximum as a statistic. On the right hand side you see the maximum as a statistic, and on the left hand side you see the mean.

![priorPred](/images/priorPredCheck.png)

This is a check of predictive accuracy of both models, for all cases, ordered from greates to smallest.
