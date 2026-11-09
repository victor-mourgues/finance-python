"""

Minimum variance hedge ratio on real market data (yfinance).

The hedge ratio that minimises the variance of the hedged position is h* = rho * sigma_A / sigma_B = Cov(A, B) / Var(B)
where A is the hedged asset, B the hedging instrument and rho the correlation of their daily log returns. h* is also the beta of A against B.

Hedge effectiveness is rho^2 (share of the variance of A removed by the hedge).
The remaining risk (1 - rho^2) is basis risk: it is specific to A and cannot be hedged with B.

Example: Apple hedged with the S&P 500.

"""

import numpy as np
import pandas as pd
import yfinance as yf

START, END = "2024-10-25", "2026-10-23"

"""

A. Download the daily closing prices of a ticker from Yahoo Finance

"""

def get_prices(ticker):
    return yf.Ticker(ticker).history(start=START, end=END)["Close"]

"""

B. Calculate the daily log returns ln(P_t / P_{t-1})

"""

def log_returns(prices):
    return np.log(prices / prices.shift(1)).dropna()

"""

C. Return (rho, h*) for `asset` hedged with `hedge_instrument`

Both return series are aligned on common dates before computing the correlation and the standard deviations

"""

def hedging(asset, hedge_instrument):
    returns_a = log_returns(get_prices(asset))
    returns_b = log_returns(get_prices(hedge_instrument))

    # Keep only the dates present in both series
    data = pd.concat([returns_a, returns_b], axis=1, keys=["A", "B"]).dropna()

    rho = data["A"].corr(data["B"])
    h = rho * data["A"].std() / data["B"].std()
    return rho, h


if __name__ == "__main__":
    rho, h = hedging("AAPL", "^GSPC")
    print("Correlation:", round(rho, 3),
          "| h*:", round(h, 3),
          "| rho^2:", round(rho ** 2, 3))

    # Example: hedge a 1,000,000 long position in Apple with the index
    position = 1_000_000
    print("Short", round(h * position), "of the index to hedge the position")
