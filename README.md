# finance-python

Python exercises for market finance, built while preparing for sales, structuring and trading roles. Each folder is a self-contained topic with commented code and a small example at the bottom of the file.

## Contents

| Folder | What it does |
|---|---|
| `oop/` | Object-oriented programming: a bank account class and a `Portfolio` class that tracks trades, net position and average buy price. |
| `returns_volatility/` | Simple and log returns with pandas, annualised volatility (daily std x sqrt(252)), volatility comparison across assets. |
| `hedging/` | Minimum variance hedge ratio h* = rho x sigma_A / sigma_B on real market data (Apple vs S&P 500), with hedge effectiveness rho^2. |
| `monte_carlo/` | Simulation of 10,000 strategies over 252 days, central limit theorem, and the probability of a loss over one year (simulation vs normal formula). |

## Key concepts

- Log returns are additive over time; annual volatility scales with the square root of time.
- The minimum variance hedge ratio is the beta of the asset against the hedging instrument.
- Monte Carlo estimates converge to the theoretical value at a rate of 1/sqrt(N).
- A sum of many independent shocks is approximately normal (central limit theorem).

## Stack

Python, NumPy, pandas, matplotlib, SciPy, yfinance.

## Run
