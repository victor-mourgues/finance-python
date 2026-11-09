"""
Bond pricing: present value of future cash flows.

Price = sum of C / (1 + y)^t + N / (1 + y)^T
with C the annual coupon, N the nominal, y the yield and T the maturity.

- Loop version and vectorised NumPy version of the same formula.
- Price-yield curve: the price falls when the yield rises, and the curve is
  convex (not a straight line).
"""

import numpy as np
import matplotlib.pyplot as plt

"""
A. Price a bond with annual coupons, using a loop
Checks: bond_price(100, 0.05, 0.04, 3) ~ 102.775 
        bond_price(100, 0.05, 0.05, 3) = 100 
        (yield = coupon: priced at par)
"""

# Bond price with a loop: PV of each coupon, plus PV of the nominal
def bond_price(nominal, coupon_rate, y, T):
    prix = 0

    # Adding the coupons' PVs
    for i in range(T):
        prix += (coupon_rate * nominal) / (1 + y) ** (T - i)

    # Adding the nominal's PV
    prix += nominal / (1 + y) ** T

    return prix

"""
B. Same price without a loop (vectorised version), using NumPy
"""

def bond_price_np(nominal, coupon_rate, y, T):
    t = np.arange(1, T + 1)                   # [1, 2, 3]: years of the cash flows
    flux = np.full(T, coupon_rate * nominal)  # [5, 5, 5]: coupons
    flux[-1] += nominal                       # last cash flow: 5 + 100 = 105
    return (flux / (1 + y) ** t).sum()        # present values, then sum


"""
C. Compute the price for yields from 1% to 10% and plot price vs yield
"""

def plot_price_yield(nominal=100, coupon_rate=0.05, T=3):
    taux = np.arange(0.01, 0.101, 0.005)      # 1% to 10%, step 0.5%
    prix = []
    for y in taux:
        prix.append(bond_price(nominal, coupon_rate, y, T))

    plt.plot(taux, prix)
    plt.title("Bond price vs interest rate")
    plt.xlabel("Yield")
    plt.ylabel("Bond price")
    plt.show()

"""
D. Reading the curve.
1) When the yield rises, the price falls: future cash flows are discounted at a higher rate, so their present values are smaller.
2) The curve is not a straight line: it is convex. From 1% to 4% the price falls by ~8.99, but from 4% to 7% only by ~8.02.
"""

if __name__ == "__main__":
    print(bond_price(100, 0.05, 0.04, 3))      # ~ 102.775
    print(bond_price(100, 0.05, 0.05, 3))      # 100
    print(bond_price_np(100, 0.05, 0.04, 3))   # same as the loop version
    print(bond_price_np(100, 0.05, 0.05, 3))   # 100

    # Convexity check: price changes over two equal yield intervals
    p1, p4, p7 = (bond_price(100, 0.05, y, 3) for y in (0.01, 0.04, 0.07))
    print("Price change 1% -> 4%:", p1 - p4)
    print("Price change 4% -> 7%:", p4 - p7)

    plot_price_yield()
