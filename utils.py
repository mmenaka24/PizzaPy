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


def read_csv_as_dict(filename: str) -> dict[str, list[str]]:
    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        headers = reader.fieldnames
        items = list(reader)

    if not headers:
        raise ValueError("Could not find CSV headers")

    csv_as_dict = {h: [] for h in headers}

    if not items:
        raise ValueError("CSV file is empty")

    for i in items:
        for h in headers:
            csv_as_dict[h].append(i[h])

    return csv_as_dict
