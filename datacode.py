import pandas as pd

# ==========================
# LOAD DATASETS
# ==========================

trades = pd.read_csv("historical_data.csv")
sentiment = pd.read_csv("fear_greed_index.csv")

print("\nTrades Shape:", trades.shape)
print("Sentiment Shape:", sentiment.shape)

print("\nMissing Values in Trades:")
print(trades.isnull().sum())

print("\nMissing Values in Sentiment:")
print(sentiment.isnull().sum())

print("\nDuplicate Trades:")
print(trades.duplicated().sum())

print("\nDuplicate Sentiment Rows:")
print(sentiment.duplicated().sum())
# ==========================
# CHECK DATA
# ==========================

print("Trades Columns:")
print(trades.columns.tolist())

print("\nSentiment Columns:")
print(sentiment.columns.tolist())

# ==========================
# CONVERT DATES
# ==========================

trades['Timestamp IST'] = pd.to_datetime(
    trades['Timestamp IST'],
    format='%d-%m-%Y %H:%M'
)

trades['date'] = trades['Timestamp IST'].dt.date

sentiment['date'] = pd.to_datetime(
    sentiment['date']
).dt.date

# ==========================
# MERGE DATASETS
# ==========================

merged = pd.merge(
    trades,
    sentiment[['date', 'classification']],
    on='date',
    how='left'
)

# ==========================
# VERIFY MERGE
# ==========================

print("\nMerged Dataset Shape:")
print(merged.shape)

print("\nClassification Counts:")
print(merged['classification'].value_counts(dropna=False))

print("\nTrade Date Range:")
print(trades['date'].min(), "to", trades['date'].max())

print("\nSentiment Date Range:")
print(sentiment['date'].min(), "to", sentiment['date'].max())

# ==========================
# CLEAN NUMERIC COLUMNS
# ==========================

numeric_cols = [
    'Closed PnL',
    'Size USD',
    'Execution Price',
    'Fee'
]

for col in numeric_cols:
    merged[col] = pd.to_numeric(
        merged[col],
        errors='coerce'
    )

# ==========================
# PROFITABILITY ANALYSIS
# ==========================

profit_summary = merged.groupby(
    'classification'
)['Closed PnL'].agg(
    ['count', 'mean', 'median', 'sum']
)

print("\nProfitability Summary:")
print(profit_summary)

# ==========================
# WIN RATE ANALYSIS
# ==========================

merged['Win'] = merged['Closed PnL'] > 0

win_rate = merged.groupby(
    'classification'
)['Win'].mean() * 100

print("\nWin Rate (%):")
print(win_rate)

# ==========================
# TRADING ACTIVITY
# ==========================

trade_count = merged.groupby(
    'classification'
).size()

print("\nTrade Count:")
print(trade_count)

# ==========================
# BUY VS SELL ANALYSIS
# ==========================

side_analysis = pd.crosstab(
    merged['classification'],
    merged['Side']
)

print("\nBuy/Sell Analysis:")
print(side_analysis)

# ==========================
# TOP 10 COINS
# ==========================

coin_profit = merged.groupby(
    'Coin'
)['Closed PnL'].sum()

coin_profit = coin_profit.sort_values(
    ascending=False
)

print("\nTop 10 Coins by Profit:")
print(coin_profit.head(10))

long_short_ratio = pd.crosstab(
    merged['classification'],
    merged['Side'],
    normalize='index'
) * 100

print("\nLong/Short Ratio (%):")
print(long_short_ratio)
# ==========================
# TOP 10 TRADERS
# ==========================

top_traders = merged.groupby(
    'Account'
)['Closed PnL'].sum()

top_traders = top_traders.sort_values(
    ascending=False
)

print("\nTop 10 Traders:")
print(top_traders.head(10))

# ==========================
# FINAL SUMMARY TABLE
# ==========================

summary = merged.groupby(
    'classification'
).agg(
    Trades=('Closed PnL', 'count'),
    AvgPnL=('Closed PnL', 'mean'),
    TotalPnL=('Closed PnL', 'sum'),
    AvgTradeSize=('Size USD', 'mean'),
    AvgFee=('Fee', 'mean')
)

print("\nFinal Summary:")
print(summary)

print("\nDataset Summary")
print("-" * 40)

print(f"Trades Rows: {trades.shape[0]}")
print(f"Trades Columns: {trades.shape[1]}")

print(f"Sentiment Rows: {sentiment.shape[0]}")
print(f"Sentiment Columns: {sentiment.shape[1]}")
# ==========================
# SAVE MERGED FILE
# ==========================

trade_freq = merged.groupby('Account').size()

median_freq = trade_freq.median()

frequent_traders = trade_freq[trade_freq >= median_freq]
infrequent_traders = trade_freq[trade_freq < median_freq]

print("\nFrequent Traders:", len(frequent_traders))
print("Infrequent Traders:", len(infrequent_traders))

trader_pnl = merged.groupby(
    'Account'
)['Closed PnL'].sum()

winning_traders = trader_pnl[trader_pnl > 0]
losing_traders = trader_pnl[trader_pnl <= 0]

print("\nWinning Traders:", len(winning_traders))
print("Losing Traders:", len(losing_traders))

volume = merged.groupby(
    'Account'
)['Size USD'].sum()

median_volume = volume.median()

high_volume = volume[volume >= median_volume]
low_volume = volume[volume < median_volume]

print("\nHigh Volume Traders:", len(high_volume))
print("Low Volume Traders:", len(low_volume))

merged['LossTrade'] = merged['Closed PnL'] < 0

drawdown_proxy = (
    merged.groupby('classification')['LossTrade']
    .mean() * 100
)

print("\nLoss Rate by Sentiment (%):")
print(drawdown_proxy)

merged.to_csv(
    "merged_analysis.csv",
    index=False
)

print("\nMerged file saved as merged_analysis.csv")