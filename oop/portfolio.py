"""
Portfolio: a trade-based position tracker.

- add_trade(ticker, qty, price) records buys (qty > 0) and sells (qty < 0).

- get_position(ticker) returns the net position and the average buy price (total buy value / total bought quantity). 
Sells reduce the net position but do not change the average buy price.

"""


class Portfolio:
    def __init__(self):
        self.net_qty = {}       # ticker -> net quantity (buys - sells)
        self.buy_value = {}     # ticker -> total amount spent on buys
        self.buy_qty = {}       # ticker -> total quantity bought

    def add_trade(self, ticker, qty, price):
        """Record a trade: qty > 0 for a buy, qty < 0 for a sell."""
        self.net_qty[ticker] = self.net_qty.get(ticker, 0) + qty
        if qty > 0:
            self.buy_value[ticker] = self.buy_value.get(ticker, 0) + qty * price
            self.buy_qty[ticker] = self.buy_qty.get(ticker, 0) + qty

    def get_position(self, ticker):
        """Return the net position and the average buy price of a ticker."""
        if ticker in self.buy_qty:
            avg = self.buy_value[ticker] / self.buy_qty[ticker]
        else:
            avg = None          # never bought: no buy price
        return {"net_position": self.net_qty.get(ticker, 0),
                "avg_price": avg}

#Execution

if __name__ == "__main__":
    p = Portfolio()
    p.add_trade("AAPL", 100, 150)
    p.add_trade("AAPL", 50, 160)
    p.add_trade("AAPL", -30, 170)
    print(p.get_position("AAPL"))
