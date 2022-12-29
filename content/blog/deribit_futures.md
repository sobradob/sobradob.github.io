---
title: The Quest for Perp AMMs
description: Article on decentralised perpetual futures for Deribit Insights. Co-authored with Dr. Abdulla Al-Kamil.
toc: true
tags:
categories:
- Derivatives
- Finance
- Crypto
series: Finance
date: '2021-10-04T13:11:22+08:00'
featuredImage: images/deribit.jpeg
draft: false

---
*Originally published in [Deribit Insights](https://www.wired.com/story/crypto-remittances-cuba/). Co-authored with Dr. Abdulla Al-Kamil.*

What are perpetual futures?
---------------------------

Perpetual swaps (also known as perpetual futures or perps) are the most widely used derivative product in crypto. Perps are futures contracts with no expiration or settlement. Instead of expiring on a given day, a funding rate mechanism is used to tie the price to an index of the price of the underlying asset. The funding rate mechanism is simple, several times a day participants must pay each other based on the imbalance between mark price and index price:

-   if the mark price is over the index price, longs pay shorts
-   if the mark price is under the index price, shorts pay longs

Perps are by far the most popular crypto speculation product: the vast majority of the multi trillion dollar crypto derivatives volume comes from perpetual swaps. Derivatives volumes are usually multiples higher than spot volumes. As such, fees from perpetual swaps are a significant source of income for crypto exchanges like Deribit, Binance and FTX. Part of the reason they are popular is that they provide an easy way for retail traders to execute high leverage trades, with up to x125 leverage. Perhaps due to their success, these products have increasingly come under regulatory scrutiny. Retail access to crypto-derivatives was restricted this year in the [UK](https://www.fca.org.uk/news/press-releases/fca-bans-sale-crypto-derivatives-retail-consumers), may soon be restricted in China and has been restricted for a while in the USA.

Decentralised Perpetual Futures
-------------------------------

Given regulatory pressures on crypto derivatives and the proven product market fit of decentralised spot exchanges such as Uniswap, Curve and Sushi, it makes sense to monitor decentralised perpetual swap exchanges. Many of these exchanges are operational and have been producing significant volumes. At their peak, DEXes produced 700m dollars in volume in 24 hours. Volumes, unlike that of CEXs, have already recovered since their May peaks.

[![](https://insights.deribit.com/wp-content/uploads/2021/10/3847gruv.jpg)](https://insights.deribit.com/wp-content/uploads/2021/10/3847gruv.jpg)

Decentralised perpetuals platforms can generally be categorised into two:

-   Central Limit Order Book (CLOB) based products (such as DyDX and Mango Markets)
-   Automated Market Maker (AMM) based products (such as Perpetual Protocol and FutureSwap)

There is considerable innovation in both architectures, and each of them have advantages and disadvantages. Yet they all share in common one thing: a need for low gas costs. Perpetual Protocol is currently operational on xDai , Futureswap V3 will be launching on Arbitrum, Mango Markets runs on Solana and DyDX has launched its layer two solution on Starkware.

Replicating the Uniswap's success? CLOB vs AMMs
-----------------------------------------------

CLOB based architectures are the golden standard of CEXes and have proven to be a successful model. Within the DEX space, CLOB products have to deal with some of the same issues as CEXes, such as finding active market makers and providing liquidity. However, CEXes have significantly higher computational needs and are therefore proving to be difficult to implement in a decentralised way. For instance, DyDx utilises an off-chain engine to match orders. This sacrifices some of the advantages of on-chain execution, such as censorship-resistance.

Other platforms, such as Perpetual Protocol and FutureSwap are trying to adapt the AMM based models to the world of derivatives. AMM models have been a resounding success in the crypto spot markets. The advantage that DEX AMMs such as Uniswap have are that:

-   they are computationally cheaper than CLOBs (and therefore have cheaper gas costs)
-   they make it trivially easy for users to create new markets
-   they make it trivially easy for users to provide liquidity to existing markets

It is interesting to note that the AMM model (Perp & Futureswap) and the CLOB model (dYdX) have two different visions of the future.

Projects following the CLOB model (such as dYdX) are aiming to provide much of the same functionality and user experience that you would expect from a CEX, but in a somewhat more decentralised fashion. The AMM model (such as Perp) aims to leverage the composability of DeFi to create a new world altogether. In spot market AMMs creating markets is both permissionless and simple, which means spot DEXes can capture a long tail market of spot assets. AMMs can also create thick liquidity pools which can compete with CEX spreads. Adapting the AMM model to derivatives has proven difficult however.

AMMs and futures
----------------

The most successful AMM based futures platform, Perpetual Protocol, has pioneered a method called a virtual Automated Market Maker (vAMM). The successes and challenges of the vAMM model illustrate the difficulties of replicating the Uniswap's success with futures. For a more in depth explanation try the [official documentation](https://docs.perp.fi/) or[ this](https://greymattercapital.substack.com/p/perpetual-protocol-analysis-and-valuation) analysis.

Like on Uniswap, traders trade with a constant product AMM, not directly with each other. However, unlike with spot AMMs, there is no actual swap of assets. Rather, traders buy (or sell) a virtual directional exposure to an asset. All trades are cash settled in USDC and traders must post USDC as collateral on isolated margin positions.

Another key difference to Uniswap has to do with the liquidity provision. In Perp's current V1 model, there are no liquidity providers per se. This is achievable because the vAMM mark price can only change as a function of trades. Thus every traders gain is another traders loss, and there is mathematically no way for the vAMM to end up with more liabilities than assets. This is achievable due to a property known as path independence. However, this mathematical property does not guarantee that the given futures price will track that of the spot price of a given asset.

In order to bring the mark price of a given asset close to the index price, the protocol uses an hourly funding rate like on FTX. The index prices are provided by a Chainlink feed. Like in most other exchanges, there is an insurance fund which serves to compensate users in case of bad debt and to pay funding rates should there be an open interest imbalance.

The AMM DEX derivative experience in practice
---------------------------------------------

This model has been running on xDAI since late 2020 and has successful in that it has generated 26bn USD in volume across multiple markets (more stats can be viewed [here](https://duneanalytics.com/yenwen/perpetual-protocol_2)). However, there have been a few issues.

**Latency issues and Flash Crashes**. There have been latency issues and flash crashes during periods of high volatility. Latency issues on xDAI during periods of volatility have lead to flash crashes during periods of volatility as arbitrageurs could not step in to take the other side of large liquidated positions, nor could individuals adjust their margin. This has been resolved through network upgrades on xDAI and a more generous liquidation engine that liquidates positions based on the index price rather than the mark price (like Binance). There were no flash crashes during the latest period of volatility, so the issue appears to be resolved.

**Low number of traders**. It has been hard to attract individual traders to the platform. In the last 7 days, while there has been 523.5m USD in volume, there have only been 390 distinct traders. This means that most of the traders are arbitrageurs and bots, with the AMM insurance fund indirectly taking the other side. So far the comparatively greater friction of using a DEX versus using a CEX is too high to bring a significant number of retail speculators on board. CEXes remain easily available for many, while DEXes are still comparatively cumbersome to use. This is likely to change with time, as regulatory pressure limits down centralised markets and the UX of DEXes improves. Nonetheless, the current prevalence of arbitrageurs and bots means that [toxic flow](https://insights.deribit.com/market-research/toxic-flow-its-sources-and-counter-strategies/) is pervasive, and this exacerbates the open interest imbalance (more on this later).

**Funding rate bleed**. Perpetual Protocol currently has abnormal funding rates compared to all other futures perpetual exchanges. Perp Exchange is persistently by far the cheapest place to long ETH and BTC, with persistently negative funding rates even during the height of market euphoria. This is an opportunity for arbitrageurs that the Perpetual Protocol team has openly publicised. A leveraged delta neutral position, with longs on [Perp.Exchange](http://perp.exchange/) and shorts elsewhere can be surprisingly profitable. Following a 2x long ETH-USDC on Perp and 2x short ETH-PERP in FTX would have yielded over 100% APR since the market was opened. Moreover, this yield can be compounded *every hour*.

While this is an opportunity for traders and arbitrageurs, it is a significant problem for the protocol. The reason being that there is generally an imbalance between long and short open interest, so the funding rate is not merely paid by traders to each other. Unlike with CLOB models, where short OI always equals long OI, in the vAMM model the two must be unequal unless the mark price of the asset is equal to its opening price.

An example may serve to illustrate why. Say a market opens with the mark price of 1 ETH = 1000 USDC and zero open interest. Alice decides to take a long position. In this case, the OI will increase by the size of Alice's nominal position, and the mark price increase to 1 ETH > 1000 USDC. Should Alice decide to close her position, or should Bob decide to open a short of the same nominal size as Alices' the ETH mark price will return to 1000 USDC.

From this it follows that the ***net open interest determines the deviation from the opening price***. Due to the principle of path independence, the only way the price can go up from the opening price to higher multiples is if people buy a long ETH-USDC contract. Not only must they long ETH-USDC, they must also keep their position open.

See below, the price of Sushi on Perp is mirrored by the net OI:

[![](https://insights.deribit.com/wp-content/uploads/2021/10/8347grhfsuh.jpg)](https://insights.deribit.com/wp-content/uploads/2021/10/8347grhfsuh.jpg)[![](https://insights.deribit.com/wp-content/uploads/2021/10/weybf9kki.jpg)](https://insights.deribit.com/wp-content/uploads/2021/10/weybf9kki.jpg)

On 14 December 2020, the ETHUSDC pair was created on perp.exchange. The initial price for ETH was 584.74 USDC. At the time of writing this article, ETH is currently multiples higher. ***The further away an asset is from its opening price, the more OI is required to sustain it there***.

Unlike in CLOBs where speculators are usually compensated via the funding payment for taking up an unpopular position, on the Perp vAMM there is a payment to arbitrageurs for bringing the price closer to the mark price. The more OI is required, the higher the funding rate needs to be to attract more capital.

[![](https://insights.deribit.com/wp-content/uploads/2021/10/93573948f.jpg)](https://insights.deribit.com/wp-content/uploads/2021/10/93573948f.jpg)

If there is an imbalance between short OI and long OI, the insurance fund has to step in to pay (or be paid) the difference. Thus, unlike in CLOBs, the funding is not being paid only by traders to each other, but rather often from the insurance fund to the traders (or vice versa).

These funding payments are to a large extent counteracted by the 10 bps tx fee that the protocol produces, but this depends on the volatility of the market and the trade volume. Effectively, the protocol's insurance fund is short vol, and suffered a slow bleed at the hands of arbitrageurs when the markets were volatile. It had to be topped up in May. It has thrived however, in the last few months of sideways price action:

[![](https://insights.deribit.com/wp-content/uploads/2021/10/8wygehuvn.jpg)](https://insights.deribit.com/wp-content/uploads/2021/10/8wygehuvn.jpg)

Lessons from AMM based perpetuals
---------------------------------

Given the experience with V1, the Perpetual Protocol team is building an entirely new architecture for Perp V2. Perp V2 requires a more active market making strategy, to avoid the funding bleed of the V1 model. It will leverage Uniswap V3, and is betting that the solution to decentralised Perpetuals lies in a compromise between the CLOB and AMM model.

The key value of the AMM model is the ability to easily and permissionlessly create new markets. As of yet, none of the protocols are able to offer that. The first protocol to crack a sustainable model, where users are incentivised to create their own perpetual futures markets on anything with a price feed, is likely to see a significant moat.

While the decentralised perpetual swap market is still in its infancy, there are a few things that are clear. First, we know from the CEX world that perpetual swaps are some of the most popular speculative products in crypto. Second, it is also evident that regulators are no longer showing a blind eye to offshore exchanges offering 100x leverage with no KYC. Third, there is a considerable appetite for KYC-free decentralised exchanges. It remains to be seen how we get there, but it is likely that within a year a far greater share of the volume will happen on decentralised exchanges.
