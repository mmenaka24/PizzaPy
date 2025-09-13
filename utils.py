import csv
import sys


def check_command_line_args() -> None:
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")


def check_file_is_csv_file(filename: str) -> None:
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")


def read_csv_as_dict(filename: str) -> dict[str, str]:
    items = []
    headers = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            items.append(row)

        headers = reader.fieldnames
        if not headers:
            sys.exit("Error: Could not find CSV headers")

    if len(items) == 0:
        sys.exit("Error: CSV file is empty")

    csv_as_dict = {}

    for h in headers:
        csv_as_dict[h] = []

    for i in items:
        for h in headers:
            csv_as_dict[h].append(i[h])

    return csv_as_dict
