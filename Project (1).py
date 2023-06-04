import yfinance as yf
import matplotlib.pyplot as plt

tickers = ["MC.PA", "OR.PA"]

returns = yf.download(tickers, start="2022-01-01", end="2022-12-31")["Close"].pct_change()

arr = []
for ticker in tickers:
    autocorr_arr = []
    for i in range(1, 11):
        autocorr_arr.append(returns[ticker].autocorr(lag=i))
    arr.append(autocorr_arr)

figure, ax = plt.subplots(2, 1, figsize=(10, 10))
for i, ticker in enumerate(tickers):
    ax[i].bar(range(1, 11), arr[i])
    if i == 0:
        ax[i].set_title("Louis Vuiton")
    if i == 1:
        ax[i].set_title("L'Oreal")
plt.show()

correlation = returns.corr(method="pearson")
figure, ax = plt.subplots(figsize=(10, 10))
im = ax.imshow(correlation, cmap="Spectral")
ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.set_xticklabels(tickers)
ax.set_yticklabels(tickers)
plt.colorbar(im, ax=ax)
plt.show()
