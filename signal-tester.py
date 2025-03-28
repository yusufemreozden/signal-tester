# ************************************************************************** #
#                                                                            #
#    Signal Tester                                                           #
#                                                                            #
#    By: Yusuf Emre OZDEN | <yusufemreozdenn@gmail.com>                      #
#                                                                            #                                            
#    https://GitHub.com/yusufemreozden                                       #
#    https://linkedIn.com/in/yusufemreozden                                  #
#                                                                            #
# ************************************************************************** #

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# === Kullanıcı Girişi ===
ticker = input("Borsa İstanbul hisse senedi sembolünü girin (örnek: TUPRS): ").upper()
start = input("Veri için başlangıç tarihini girin (örnek: 2019-01-01): ")
end = input("Veri için bitiş tarihini girin (örnek: 2025-03-28): ")

# BIST için .IS kodu ekleme
if not ticker.endswith(".IS"):
    ticker += ".IS"

# === Veri Çekme ===
df = yf.download(ticker, start=start, end=end)

if df.empty:
    print("Veri alınamadı.")
    exit()

# === Göstergeler ===
df["EMA13"] = df["Close"].ewm(span=13, adjust=False).mean()
df["EMA55"] = df["Close"].ewm(span=55, adjust=False).mean()

# === Sinyal Üretimi ===
df["Signal"] = 0
df.loc[df["EMA13"] > df["EMA55"], "Signal"] = 1
df.loc[df["EMA13"] < df["EMA55"], "Signal"] = -1
df["Cross"] = df["Signal"].diff()

buy_signals = df[df["Cross"] == 2]
sell_signals = df[df["Cross"] == -2]

# === Grafik ===
plt.figure(figsize=(14, 6))
plt.plot(df.index, df["Close"], label="Close Price", linewidth=1.2)
plt.plot(df.index, df["EMA13"], label="EMA13", linestyle="--", color="orange")
plt.plot(df.index, df["EMA55"], label="EMA55", linestyle="--", color="green")
plt.scatter(buy_signals.index, buy_signals["Close"], label="Buy", marker="^", color="green")
plt.scatter(sell_signals.index, sell_signals["Close"], label="Sell", marker="v", color="red")
plt.title(f"{ticker} EMA13/EMA55 Crossover Strategy")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("signal_plot.png")
plt.show()

# === Performans Analizi ===
buy_prices = buy_signals["Close"].values
sell_prices = sell_signals["Close"].values
num_trades = min(len(buy_prices), len(sell_prices))

profits = []
for i in range(num_trades):
    profit = sell_prices[i] - buy_prices[i]
    profits.append(profit)

# Güncellenmiş biçimlendirme
total_profit = float(sum(profits))
avg_profit = total_profit / len(profits) if profits else 0.0
win_trades = [p for p in profits if p > 0]
win_rate = len(win_trades) / len(profits) * 100 if profits else 0.0

# === Sonuçlar ===
print("\n=== Backtest Sonuçları ===")
print(f"Toplam İşlem Sayısı: {len(profits)}")
print(f"Başarılı İşlem Sayısı: {len(win_trades)}")
print(f"Başarı Oranı: %{win_rate:.2f}")
print(f"Toplam Kar: {total_profit:.2f} ₺")
print(f"Ortalama Kar/Zarar: {avg_profit:.2f} ₺")
