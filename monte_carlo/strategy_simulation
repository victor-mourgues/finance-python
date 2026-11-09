"""

Monte Carlo simulation of 10,000 strategies over 252 trading days.

- Coin flips: average gain and standard deviation of one game.
- Daily log returns drawn from N(0.05%, 1%) with a seeded NumPy generator.
- Annual log return of each strategy = sum of daily returns (axis=1).
- Central limit theorem: histogram of the 10,000 annual returns.
- Probability of a loss over one year: simulated proportion of negative
  outcomes (loop and vectorised) vs. the closed-form normal formula
  Phi(-mu_T / sigma_T).
  
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

MU, SIGMA, N_DAYS = 0.0005, 0.01, 252

"""

A. Simulate 10,000 coin flips (+1 EUR for heads, -1 EUR for tails)
Compute the average gain and the standard deviation of one game

"""

def coin_flips(rng, n=10_000):
    flips = rng.choice([-1, 1], size=n)
    return flips.mean(), flips.std()

"""

B. Simulate 10,000 strategies over 252 days, each day with a random return of mean 0.05% and standard deviation 1%
Compute the cumulative log return of each strategy

"""

def simulate_strategies(rng, n_strategies=10_000):
    daily = rng.normal(MU, SIGMA, size=(n_strategies, N_DAYS))
    return daily.sum(axis=1)

"""

# C. Central limit theorem. Plot a histogram of the 10,000 cumulative returns

"""

def plot_histogram(returns):
    plt.hist(returns, bins=50)
    plt.axvline(0, color="red")
    plt.title("Histogram of 10,000 annual log returns")
    plt.xlabel("Annual log return")
    plt.show()

"""

D. Probability of losing money over the year
V1: proportion of negative simulations (loop and vectorised)
V2: normal distribution formula

"""

# Proportion of negative returns, with a loop
def loss_proportion_loop(returns):
    count = 0
    for r in returns:
        if r < 0:
            count += 1
    return count / len(returns)

# Proportion of negative returns, vectorised (mean of booleans)
def loss_proportion_vectorised(returns):
    return (returns < 0).mean()

# P(annual return < 0) = Phi(-mu_T / sigma_T), with mu_T = n*mu, sigma_T = sigma*sqrt(n)
def loss_probability_normal(mu=MU, sigma=SIGMA, n_days=N_DAYS):
    mu_t = n_days * mu
    sigma_t = sigma * np.sqrt(n_days)
    return norm.cdf(0, loc=mu_t, scale=sigma_t)


if __name__ == "__main__":
    rng = np.random.default_rng(42)

    mean_gain, std_gain = coin_flips(rng)
    print("Coin flips: mean =", mean_gain, "| std =", std_gain)

    returns = simulate_strategies(rng)
    print("Simulated mean:", returns.mean(), "| theory:", N_DAYS * MU)
    print("Simulated std: ", returns.std(), "| theory:", SIGMA * np.sqrt(N_DAYS))

    print("P(loss), loop:      ", loss_proportion_loop(returns))
    print("P(loss), vectorised:", loss_proportion_vectorised(returns))
    print("P(loss), normal:    ", loss_probability_normal())

    plot_histogram(returns)
