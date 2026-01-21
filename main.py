import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
sentiment_df = pd.read_csv("fear_greed_index.csv")
trades_df = pd.read_csv("historical_data.csv")

# Sentiment Dataset Processing
sentiment_df['classification'] = sentiment_df['classification'].str.lower()

# Distribution of sentiment regimes
sentiment_distribution = sentiment_df['classification'].value_counts()

# Trader Dataset Processing
trades_df['Closed PnL'] = trades_df['Closed PnL'].fillna(0)
trades_df['Fee'] = trades_df['Fee'].fillna(0)
trades_df['Net PnL'] = trades_df['Closed PnL'] - trades_df['Fee']

# Trader performance stats
total_trades = len(trades_df)
win_rate = (trades_df['Net PnL'] > 0).mean() * 100
avg_pnl = trades_df['Net PnL'].mean()

# Behavioral Insights (Proxy Analysis)
# We assume traders operate under mixed sentiment regimes

performance_summary = {
    "Total Trades": total_trades,
    "Average Net PnL": avg_pnl,
    "Win Rate (%)": win_rate
}

summary_df = pd.DataFrame(performance_summary, index=[0])
print(summary_df)

# Visualizations

# Sentiment distribution
plt.figure()
sentiment_distribution.plot(kind='bar')
plt.title("Bitcoin Market Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Days Count")
plt.show()

# Net PnL distribution
plt.figure()
plt.hist(trades_df['Net PnL'], bins=100)
plt.title("Trader Net PnL Distribution")
plt.xlabel("Net PnL")
plt.ylabel("Frequency")
plt.show()

# Risk Analysis
cumulative_pnl = trades_df['Net PnL'].cumsum()
peak = cumulative_pnl.cummax()
drawdown = cumulative_pnl - peak

plt.figure(figsize=(10,4))
drawdown.plot()
plt.title("Trader Drawdown Curve")
plt.xlabel("Trades")
plt.ylabel("Drawdown")
plt.show()
