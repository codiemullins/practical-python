import fileparse
import stock


def read_portfolio(filename):
    with open(filename) as file:
        portdicts = fileparse.parse_csv(file, types=[str, int, float])
    portfolio = [stock.Stock(d["name"], d["shares"], d["price"]) for d in portdicts]
    return portfolio


def read_prices(filename):
    with open(filename) as file:
        pricelist = fileparse.parse_csv(file, types=[str, float], has_headers=False)
        return dict(pricelist)


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    headers = ("Name", "Shares", "Price", "Change")
    print("%10s %10s %10s %10s" % headers)
    print(("-" * 10 + " ") * len(headers))
    for holding in portfolio:
        price = "$" + f"{prices[holding.name]:.2f}"
        change = prices[holding.name] - holding.price
        print(f"{holding.name:>10s} {holding.shares:>10d} {price:>10s} {change:>10.2f}")


def main(argv):
    if len(argv) == 2:
        portfolio_filename = argv[1]
    else:
        portfolio_filename = "Data/portfolio.csv"
    if len(argv) == 3:
        prices_filename = argv[2]
    else:
        prices_filename = "Data/prices.csv"
    portfolio_report(portfolio_filename, prices_filename)


if __name__ == "__main__":
    import sys

    main(sys.argv)
