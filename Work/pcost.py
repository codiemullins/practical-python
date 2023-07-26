import report


def portfolio_cost(filename: str):
    """Computes the total cost (shares*price) of a portfolio file"""
    total_cost = 0.0

    portfolio = report.read_portfolio(filename)

    for holding in portfolio:
        total_cost += holding.cost()

    return total_cost


def main(argv):
    if len(argv) == 2:
        filename = sys.argv[1]
    else:
        filename = "Data/portfolio.csv"

    cost = portfolio_cost(filename)
    print("Total cost:", cost)


if __name__ == "__main__":
    import sys

    main(sys.argv)
