# fileparse.py
#
# Exercise 3.3
import csv
import logging
log = logging.getLogger(__name__)


def parse_csv(
    file,
    select=None,
    types=None,
    has_headers=True,
    delimiter=",",
    silence_errors=False,
):
    """
    Parse a CSV file into a list of records
    """

    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    rows = csv.reader(file, delimiter=delimiter)

    # Read the file headers
    if has_headers:
        headers = next(rows)

    # If a column selector was given, find indices of the specified columns.
    # Also narrow the set of headers used for resulting dictionaries
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    else:
        indices = []

    records = []
    for rowno, row in enumerate(rows, start=1):
        try:
            if not row:  # Skip rows with no data
                continue

            # Filter the row if specific columns were selected
            if indices:
                row = [row[i] for i in indices]

            if types:
                row = [func(val) for func, val in zip(types, row)]

            # Make a dictionary
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
        except ValueError as err:
            if not silence_errors:
                log.warning(f"Row {rowno}: Couldn't convert: {row}")
                log.debug(f"Row {rowno}: Reason: {err}")

    return records
