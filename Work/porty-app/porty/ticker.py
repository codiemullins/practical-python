from .follow import follow
import csv
from . import tableformat


def select_columns(rows, indices):
    return (tuple(row[index] for index in indices) for row in rows)


def convert_types(rows, types):
    return (tuple(func(val) for func, val in zip(types, row)) for row in rows)


def make_dicts(rows, headers):
    return (dict(zip(headers, row)) for row in rows)


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ["name", "price", "change"])
    return rows


def filter_symbols(rows, names):
    return (row for row in rows if row["name"] in names)


def ticker(portfoliofile, stocklog, fmt="txt"):
    import report

    portfolio = report.read_portfolio(portfoliofile)
    rows = parse_stock_data(follow(stocklog))
    rows = filter_symbols(rows, portfolio)

    formatter = tableformat.create_formatter(fmt)
    formatter.headings(["Name", "Price", "Change"])
    for row in rows:
        rowdata = [row["name"], f'{row["price"]:.2f}', f'{row["change"]:.2f}']
        formatter.row(rowdata)


if __name__ == "__main__":
    lines = follow("Data/stocklog.csv")
    rows = parse_stock_data(lines)
    for row in rows:
        print(row)
