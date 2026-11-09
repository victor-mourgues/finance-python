"""
Returns and volatility with pandas.

Contents:
  1. Simple returns (loop version and vectorised pct_change).
  2. Log returns, which are additive over time.
  3. Annualised volatility: daily standard deviation of log returns x sqrt(252).
  4. Volatility comparison across several assets (yfinance).

Libraries: NumPy, pandas, yfinance.
"""

import numpy as np
import pandas as pd
import yfinance as yf

START, END = "2024-10-25", "2026-10-23"


# Returns ---------------------------------------------------------------------
def simple_returns_loop(prices):
    """Simple returns with a loop (old-style version, for comparison)."""
    returns = []
    for i in range(len(prices) - 1):
        returns.append(prices.iloc[i + 1] / prices.iloc[i] - 1)
    return returns


def simple_returns(prices):
    """Simple returns, vectorised with pct_change()."""
    return prices.pct_change()


def log_returns(prices):
    """Log returns without a loop: np.log, shift(1) and dropna()."""
    values = np.log(prices / prices.shift(1))
    return values.dropna()


# Volatility ------------------------------------------------------------------
def annualised_vol(prices):
    """Daily standard deviation of log returns, annualised with sqrt(252)."""
    return log_returns(prices).std() * np.sqrt(252)


def get_prices(ticker):
    """Download the daily closing prices of a ticker from Yahoo Finance."""
    return yf.Ticker(ticker).history(start=START, end=END)["Close"]


def compare_vols(tickers):
    """Return a dictionary {ticker: annualised volatility}."""
    vols = {}
    for ticker in tickers:
        vols[ticker] = annualised_vol(get_prices(ticker))
    return vols


if __name__ == "__main__":
    # Fake price series
    prices = pd.Series([100, 102, 101, 105, 103, 107],
                       index=pd.date_range("2026-10-01", periods=6, freq="B"))
    print(log_returns(prices))
    print("Annualised vol (toy):", annualised_vol(prices))

    # Real market data
    print(compare_vols(["AAPL", "MSFT", "^GSPC"]))
