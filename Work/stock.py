class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

    def __repr__(self) -> str:
        return f"Stock('{self.name}', {self.shares}, {self.price})"
