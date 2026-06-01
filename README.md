
Executive Summary
This study analyzes the relationship between Bitcoin market sentiment (Fear & Greed Index) and trader performance using 211,224 Hyperliquid trades between May 2023 and May 2025.
The analysis reveals that market sentiment significantly influences trading outcomes. Fear periods generated the highest total profits and trading activity, while Extreme Greed produced the highest average profit per trade and win rate.
Dataset Information
Dataset 1: Bitcoin Fear & Greed Index
Columns used:
•	date 
•	classification 
•	value 
Sentiment categories:
•	Extreme Fear 
•	Fear 
•	Neutral 
•	Greed 
•	Extreme Greed 
Dataset 2: Hyperliquid Historical Trader Data
Columns used:
•	Account 
•	Coin 
•	Execution Price 
•	Size USD 
•	Side 
•	Closed PnL 
•	Fee 
•	Timestamp IST 
Total trades analyzed:
211,224

Methodology
1.	Loaded both datasets using Pandas. 
2.	Converted timestamps into date format. 
3.	Merged datasets using the date field. 
4.	Cleaned numeric columns. 
5.	Performed: 
o	Profitability analysis 
o	Win-rate analysis 
o	Trading activity analysis 
o	Buy/Sell behavior analysis 
o	Coin-level profitability analysis 
6.	Created visualizations using Matplotlib.

Key Findings
1. Fear Generated Highest Total Profit
Sentiment	Total PnL
Fear	3.36M
Extreme Greed	2.72M
Greed	2.15M
Neutral	1.29M
Extreme Fear	0.74M

Interpretation:
Fear periods created the largest cumulative profit opportunities.

2. Extreme Greed Produced Highest Average Profit
Sentiment	Average PnL
Extreme Greed	67.89
Fear	54.29
Greed	42.74
Extreme Fear	34.54
Neutral	34.31

Interpretation:
Individual trades were most profitable during strong bullish sentiment.
3. Highest Win Rate Occurred During Extreme Greed
Sentiment	Win Rate
Extreme Greed	46.49%
Fear	42.08%
Neutral	39.70%
Greed	38.48%
Extreme Fear	37.06%
Interpretation:
Trader accuracy improved significantly during Extreme Greed periods.
4. Fear Periods Had Highest Trading Activity
Sentiment	Trades
Fear	61,837
Greed	50,303
Extreme Greed	39,992
Neutral	37,686
Extreme Fear	21,400
Interpretation:
Market uncertainty encouraged more trading activity.

5. Fear Had the Largest Average Position Size
Sentiment	Avg Trade Size (USD)
Fear	7,816
Greed	5,737
Extreme Fear	5,350
Neutral	4,783
Extreme Greed	3,112
Interpretation:
Traders committed more capital during Fear periods.
6. Most Profitable Assets
Coin	Total Profit
@107	2.78M
HYPE	1.95M
SOL	1.64M
ETH	1.32M
BTC	0.87M
Interpretation:
Several alternative assets outperformed Bitcoin in cumulative profitability.

