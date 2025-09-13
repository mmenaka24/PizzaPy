import sys
from utils import check_command_line_args, check_file_is_csv_file, read_csv_as_dict
from tabulate import tabulate


def format_csv_for_display(filename: str) -> str:
    menu_as_dict = read_csv_as_dict(filename)
    return tabulate(menu_as_dict, headers="keys", tablefmt="grid")


def main():

    check_command_line_args()

    filename = sys.argv[1]

    check_file_is_csv_file(filename)

    try:
        print(format_csv_for_display(filename))
    except FileNotFoundError:
        sys.exit("File does not exist")
    except Exception as e:
        sys.exit(f"Error: {e}")


if __name__ == "__main__":
    main()
