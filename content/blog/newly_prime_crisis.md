---
title: From subprime crisis to the "newly prime" crisis
description: Credit score algorithms faced an unprecedented challenge during the Covid-19 crisis. Will we soon see the consequences?
toc: true
tags:
- opinion
categories:
featuredImage: images/equal_opportunity_credit.jpg
date: '2023-06-17T13:11:22+08:00'
draft: false
---

The Global Financial Crisis of 2007 is often blamed on irresponsible subprime lending. But what if the next financial crisis happens starts with customers with seemingly good credit scores?

According to [Wikipedia](https://en.wikipedia.org/wiki/2007%E2%80%932008_financial_crisis):

> The 2007–2008 financial crisis, or Global Financial Crisis (GFC), was a severe worldwide economic crisis that occurred in the early 21st century. It was the most serious financial crisis since the Great Depression (1929). Predatory lending targeting low-income homebuyers, excessive risk-taking by global financial institutions, and the bursting of the United States housing bubble culminated in a 'perfect storm'.

After the crisis, regulators and politicians implemented a [wide range of rules](https://en.wikipedia.org/wiki/Regulatory_responses_to_the_subprime_crisis), such as maximum loan to income ratios and "affordability stress tests", to ensure lenders would be more responsible in the future. Superficially, they seem to have succeeded. For example, credit card delinquencies in the US remain well below the pre-2009 average (as are [mortgages](https://fred.stlouisfed.org/series/DRSFRMACBS)).

 <div class="embed-container"><iframe src="https://fred.stlouisfed.org/graph/graph-landing.php?g=15Hax&width=670&height=475" scrolling="no" frameborder="0" style="overflow:hidden;" allowTransparency="true" loading="lazy"></iframe></div><script src="https://fred.stlouisfed.org/graph/js/embed.js" type="text/javascript"></script>

Yet the Covid-19 pandemic caused a lot of things in the economy to "break" in non-obvious ways. The [supply chain crisis](https://en.wikipedia.org/wiki/2021%E2%80%932023_global_supply_chain_crisis) is often mentioned in the news and consumers have noticed shortages of everything from [computer chips](https://en.wikipedia.org/wiki/2020%E2%80%93present_global_chip_shortage) to [eggs](https://www.standard.co.uk/news/uk/egg-shortage-supermarkets-bird-flu-cost-of-living-b1040104.html). In an interconnected economy, it is often hard to predict how problems will flow downstream. For instance, Ken Jarosch claimed that a shortage of microchips led to reduced production of cars, which led to reduced demand for the leather used for car seats, which led to fewer pigs being slaughtered for their hides, which led to a gelatin shortage. Gelatin is a big ingredient in gummy bears and other snacks, so there was a [gummy bear shortage](https://www.bloomberg.com/news/articles/2022-12-22/odd-lots-podcast-how-a-semiconductor-shortage-impacts-gummy-bears-supply#xj4y7vzkg).

A similar story of unintended consequences might be brewing in the consumer credit market.

## The stimmies

During the pandemic the US government (and many other governments worldwide) gave out generous handouts. In the USA these were colloquially known as "stimmies" and were effectively wealth transfers from the government to the consumer. FiveThirtyEight [reports](https://fivethirtyeight.com/features/were-the-stimulus-checks-a-mistake/) that:

> According to the U.S. Census Bureau’s supplemental poverty measure, the stimulus payments moved 11.7 million people out of poverty in 2020 — a drop in the poverty rate from 11.8 to 9.1 percent. And the 2021 poverty rate was estimated to fall even further to 7.7 percent.

People also simply spent less because they were sat at home instead of going out to restaurants and travelling. Some people spent this surplus money meme-stocks or crypto or NFTs. But many others simply paid back a lot of their credit card balances and other loans. In Q4 2019, consumers credit card balances at large banks were 714 USD billion. By Q1 2021 balances dropped to 566 USD billion.

<div class="embed-container"><iframe src="https://fred.stlouisfed.org/graph/graph-landing.php?g=16f8K&width=670&height=475" scrolling="no" frameborder="0" style="overflow:hidden;" allowTransparency="true" loading="lazy"></iframe></div>

This unprecedented deleveraging of consumer credit had two consequences:
1. Consumer credit scores increased.
2. Credit card companies started to make less money.

The combination of the two may have lead to lending that was superficially responsible, but effectively disastrous.

## Credit Scores & Credit Utilisation

Credit scores try to estimate the likelihood that a costumer will pay back a loan. Most consumers have a credit score and credit scores can change over time. For example, if you just turned 18 and have no credit history, your credit score is not goint to be stellar. It would be irresponsible for a lender to give an 18 year old with no credit history thousands of dollars, unless it comes in the form of government subsidised student loans. But as you build up a history of good behaviour, your credit score will improve and lenders will be more willing to lend to you at their own risk. Although credit scores are a numerical value, credit analysts tend to bucket them into five categories for ease of reporting. These are, from bad to good:

1. Deep subprime
2. Subprime
3. Near-prime
4. Prime
5. Superprime

Every year people can transition from one bucket to another. In normal, pre-pandemic years most superprime and subprime consumers tend to stay in their respective credit score bin, with quite a bit more movement in the middle categories. For example, 24% of near-prime customers go down a credit score category whereas 37% go up.

![Pre-Pandemic Credit Score transtions](/images/pre_pandemic_credit_transitions.jpeg)

The exact way in which credit scores are calculated is the "magic sauce" of the credit bureaus. But in general terms, past behaviour tends to be a good predictor of future behaviour. So consumer credit scores tend to increase when consumers pay back their loans. Moreover, when consumers pay back their loans their credit utilisation goes down. Credit rating agency [Experian](https://www.experian.com/blogs/ask-experian/credit-education/score-basics/credit-utilization-rate/) explains what it is and why it is important:

> Your credit utilization rate, sometimes called your credit utilization ratio, is the amount of revolving credit you're currently using divided by the total amount of revolving credit you have available. In other words, it's how much you currently owe divided by your credit limit [...] Credit scoring models often consider your credit utilization rate when calculating a credit score for you. They can impact up to 30% of a credit score (which makes them among the more influential factors), depending on the scoring model being used. A low credit utilization rate shows you're using less of your available credit. Credit scoring models generally interpret this as an indication you're doing a good job managing credit by not overspending, and keeping your spending in check can help you reach higher credit scores.

In other words, consumers used government subsidies during the pandemic to pay back their credit card loans and as a consequence their credit utilisation went down.

<div class="embed-container"><iframe src="https://fred.stlouisfed.org/graph/graph-landing.php?g=16fdE&width=670&height=475" scrolling="no" frameborder="0" style="overflow:hidden;" allowTransparency="true" loading="lazy"></iframe></div>

This lead to an unprecedented inflation in credit scores. People were less likely lose credit score points, and much more likely to gain them. Forty-three percent of consumers with subprime credit scores moved up at least one tier during the pandemic, whereas in the ten years prior to the pandemic, only 37 percent moved up at least one tier.

![Post-Pandemic Credit Score transtions](/images/pandemic_credit_transitions.jpeg)

The credit score transition charts come from [this report](https://www.consumerfinance.gov/about-us/blog/office-of-research-blog-credit-score-transitions-during-the-covid-19-pandemic/) by the Consumer Finance Protection Bureau, where they explain:

> The improvements in consumer credit scores during the pandemic were driven by consumers with deep subprime and subprime credit scores, but consumers in every credit score tier were more likely to transition to a higher tier and less likely to transition to a lower tier than before. Notably, the falling share of consumers with deep subprime and subprime credit scores was not only due to transitions out of these tiers, but also because of reduced rates of transition into these tiers.

As a consequence the median credit score of credit card account holders went up, peaking at 768 in Q2 2021.

<div class="embed-container"><iframe src="https://fred.stlouisfed.org/graph/graph-landing.php?g=16fdG&width=670&height=475" scrolling="no" frameborder="0" style="overflow:hidden;" allowTransparency="true" loading="lazy"></iframe></div>

## Revolvers

Credit card companies largely depend on interest income. If credit card balances go down, so does their revenue. Their favourite type of consumer is a "revolver", someone who carries balances over from one month to the next. About half of credit card holders are revolvers and they generate most revenue for credit card companies. In fact, the Federal Reserve recently [ published a paper](https://www.federalreserve.gov/econres/feds/who-pays-for-your-rewards-redistribution-in-the-credit-card-market.htm) claiming that credit card rewards are a wealth redistribution programme from the poor and uneducated revolvers to the wealthy educated non-revolvers to the tune of $15bn dollars a year.

To compensate for the decline in revenues, credit card companies started issuing more and more cards. TransUnion, another credit rating agency, reports that there was a strong uptick in originations from Q2 2021 till late 2022.

![Credit Card Balances by Risk Band](/images/cc_origination_by_risk_band.jpeg)

By 2023 credit card balances recovered. Thanks to regulation and more responsible lending credit card companies didn't get carried away this time. Most of the credit card balances sit with customers that have "prime" credit scores or better, without irresponsible levels of subprime lending.

![Credit Card Balances by Risk Band](/images/credit_score_balance.jpeg)

## What goes around, comes around

Yet there's a problem. The performance of the 2021-2022 cohorts of loans are shocking. Near-prime customers delinquencies almost immediately looked much worse than usual. With only 12 months on book, the Q4-2021 cohort has more than double the level of delinquencies than previous Q4 cohorts.

![Credit Card Balances by Risk Band](/images/prime_performance.jpeg)

The scariest bit for lenders is that prime customers are going delinquent at the rate of historical near-prime customers. Most of the 2021-2022 credit originations by volume was in the prime segment. These are the customers that are supposed to be reliable. Current credit card delinquency rates are an issue because they suggests that lenders fundamentally mispriced a large cohort of borrowers in 2021 and 2022.

![Credit Card Balances by Risk Band](/images/prime_vs_nearprime.jpeg)

Credit models were not calibrated for unprecedented government subsides. One-off government wealth transfers were weighted the same as regular wealth increases. Credit officers of course understood this, but there was a tremendous pressure in 2021 and 2022 to issue new loans. Consumers are now paying for the government wealth transfers of 2020 and 2021 in the form of inflation and also the highest credit card interest rates in 3 decades.

<div class="embed-container"><iframe src="https://fred.stlouisfed.org/graph/graph-landing.php?g=16fw8&width=670&height=475" scrolling="no" frameborder="0" style="overflow:hidden;" allowTransparency="true" loading="lazy"></iframe></div>

Paradoxically, the ability to charge much higher interest rates quickly can offer some protection to credit card issuers from the higher delinquency rates. But not all lenders can raise interest rates for customers acquired in 2021-2022. And what else did these "newly prime" consumers buy on credit?

Mortgage originations in 2021 and 2022 were at levels not seen since the 2008 financial crisis.

<div class="embed-container"><iframe src="https://fred.stlouisfed.org/graph/graph-landing.php?g=16fwW&width=670&height=475" scrolling="no" frameborder="0" style="overflow:hidden;" allowTransparency="true" loading="lazy"></iframe></div>

Mortgage lenders cannot generally raise interest rates as quickly as credit card companies, as consumers usually lock in fixed rates. In the US mortgages are fixed for 30 years thanks to government subsidies, but even that doesn't mean that the rates risk disappears. Rather, it gets moved from the consumer to the financial institution. It is no coincidence that we've seen several bank failures in the US recently.

In other countries consumers are not so lucky. Highly leveraged, variable rate mortgage markets that were hot during the pandemic are likely to be impacted the most. Many consumers will find themselves struggling to pay an increasingly expensive mortgage for a property they overpaid for, using credit they would have not qualified for had it not been for the pandemic.

## The "Newly Prime" Crisis?

In this post I focused mostly on credit card data from USA because there is good data available and credit cards tend to show signs of trouble earlier than mortgages, but similar trends are likely to happening worldwide. The problem is that conventional credit models had no way of accounting for the COVID-19 pandemic. Meanwhile lenders were under significant pressure to issue more loans. As a result, they issued large volumes of cheap loans to people they wouldn't have lent to just a few years before.

If the risk of defaults in consumer credit markets is being significantly underestimated, the global economy might be in for a nasty surprise. And keep in mind that the current shocking performance of the 2021-2022 vintages comes during a time where the labour market is tight and unemployment is low. The strength of the labour market is in large part due to a large number of boomers who didn't return to the labour force after the pandemic. Should the labour market start showing signs of weakness, the hot real estate markets of 2021-2022 will be under significant pressure.

Credit drives the global economy. If lenders pull back due to unexpected losses, people will spend less money on consumer goods, cars and houses. The increase of interest rates has already made life difficult for many lenders. So far most negative impacts on the delinquency side have been masked by a tight labour market and strong consumer spending.  But in the US, things are likely to further deteriorate from October 2023, once student loan payments restart. The pause on student loan repayments was a significant subsidy to many consumers. Once it is removed consumer spend will take a hit and delinquencies will increase.

Will we see a recession in Q4 2023 or Q1 2024? If so, has it been priced in yet?
