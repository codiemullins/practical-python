import fileparse
import tableformat
from stock import Stock
from portfolio import Portfolio


def read_portfolio(filename, **opts):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        return Portfolio.from_csv(lines, **opts)


def read_prices(filename):
    with open(filename) as file:
        pricelist = fileparse.parse_csv(file, types=[str, float], has_headers=False)
        return dict(pricelist)


def make_report_data(portfolio, prices):
    reportdata = []
    for holding in portfolio:
        current_price = prices[holding.name]
        change = current_price - holding.price
        summary = (holding.name, holding.shares, current_price, change)
        reportdata.append(summary)
    return reportdata


def print_report(reportdata, formatter):
    """
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    """
    # headers = ("Name", "Shares", "Price", "Change")
    # print("%10s %10s %10s %10s" % headers)
    # print(("-" * 10 + " ") * len(headers))
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in reportdata:
        # price = "$" + f"{price:.2f}"
        # print(f"{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}")
        rowdata = [name, str(shares), f"{price:.2f}", f"{change:.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfoliofile, pricefile, fmt="txt"):
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    report = make_report_data(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(argv):
    if len(argv) == 2:
        portfoliofile = argv[1]
    else:
        portfoliofile = "Data/portfolio.csv"

    if len(argv) == 3:
        pricefile = argv[2]
    else:
        pricefile = "Data/prices.csv"

    if len(argv) == 4:
        fmt = argv[3]
    else:
        fmt = "txt"

    portfolio_report(portfoliofile, pricefile, fmt=fmt)


if __name__ == "__main__":
    import sys

    main(sys.argv)
