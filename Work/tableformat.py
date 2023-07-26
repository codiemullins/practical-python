class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    """
    Emit a table as a space-separated text file.
    """

    def headings(self, headers):
        for header in headers:
            print(f"{header:>10s}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        for item in rowdata:
            print(f"{item:>10s}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    """
    Emit a table in CSV format.
    """

    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """
    Emit a table in HTML format.
    """

    def headings(self, headers):
        print("<tr>", end="")
        for header in headers:
            print(f"<th>{header}</th>", end="")
        print("</tr>")

    def row(self, rowdata):
        print("<tr>", end="")
        for item in rowdata:
            print(f"<td>{item}</td>", end="")
        print("</tr>")


def create_formatter(fmt):
    if fmt == "txt":
        formatter = TextTableFormatter()
    elif fmt == "csv":
        formatter = CSVTableFormatter()
    elif fmt == "html":
        formatter = HTMLTableFormatter()
    else:
        raise RuntimeError(f"Unknown format {fmt}")

    return formatter
