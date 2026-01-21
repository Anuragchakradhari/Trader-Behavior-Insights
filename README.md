# Trader Behavior Insights: Market Sentiment vs Performance

## Objective
Analyze the relationship between Bitcoin market sentiment (Fear & Greed Index) and trader performance using historical trade data from Hyperliquid.

## Datasets
1. Bitcoin Market Sentiment Dataset  
   - Columns: Date, Classification (Fear/Greed)

2. Historical Trader Data (Hyperliquid)  
   - Includes: account, symbol, execution price, size, side, timestamp, closedPnL, leverage, etc.

## Approach
- Cleaned and preprocessed both datasets
- Calculated Net PnL, win rate, and drawdown
- Analyzed trader behavior and risk patterns
- Due to non-overlapping time periods, sentiment was treated as a macro market regime instead of forcing a misleading date-level merge

## Key Insights
- Trader PnL distribution shows high variance with risk concentration
- Drawdowns highlight exposure during volatile conditions
- Extreme sentiment regimes correlate with unstable trading outcomes

## Tools Used
- Python, Pandas, Matplotlib

## Note
This project reflects real-world data constraints and emphasizes analytical correctness over forced assumptions.
## Dataset Note
The historical trader dataset used in this project is approximately 45MB and exceeds GitHub’s file size limit.

Due to data size and privacy considerations, the raw dataset is not uploaded to this repository.
The analysis code is fully reproducible and assumes the dataset to be present locally as `historical_data.csv`.
