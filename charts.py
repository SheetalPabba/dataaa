import pandas as pd
import matplotlib.pyplot as plt

merged = pd.read_csv("merged_analysis.csv")

# Average PnL
merged.groupby('classification')['Closed PnL'].mean().plot(
    kind='bar',
    figsize=(8,5)
)
plt.title('Average PnL by Sentiment')
plt.ylabel('Average PnL')
plt.tight_layout()
plt.savefig("avg_pnl.png")
plt.close()

# Win Rate
(merged.groupby('classification')['Win']
 .mean()*100).plot(
    kind='bar',
    figsize=(8,5)
)
plt.title('Win Rate by Sentiment')
plt.ylabel('Win Rate (%)')
plt.tight_layout()
plt.savefig("win_rate.png")
plt.close()

# Trade Count
merged.groupby('classification').size().plot(
    kind='bar',
    figsize=(8,5)
)
plt.title('Trade Count by Sentiment')
plt.ylabel('Trades')
plt.tight_layout()
plt.savefig("trade_count.png")
plt.close()

print("Charts saved successfully!")