# 📈 Signal Tester – EMA Crossover Backtest Tool

This project allows you to **backtest a simple EMA crossover strategy** on Turkish BIST stocks using real historical data from Yahoo Finance.

---

## 🚀 Features

- Fetch historical price data via `yfinance`
- Calculate technical indicators: `EMA13`, `EMA55`
- Generate buy/sell signals based on EMA crossover logic
- Visualize signals on a candlestick chart
- Evaluate performance:
  - Total number of trades
  - Win rate
  - Total profit
  - Average profit/loss per trade

---

## 📌 Example Strategy

**Buy:** When EMA13 crosses above EMA55  
**Sell:** When EMA13 crosses below EMA55

---

## 🛠️ Tech Stack

- Python 3.x
- yfinance
- pandas
- matplotlib

---

## 🧠 Next Steps

- Add % profit calculation
- Export signal log to CSV
- Run multiple ticker batch tests
- Optimize EMA parameters automatically (ema-optimizer 🔜)
