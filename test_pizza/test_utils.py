import pytest
import sys
from utils import check_command_line_args, check_file_is_csv_file, read_csv_as_dict
from unittest.mock import mock_open, patch


def test_check_command_line_args_too_few_args() -> None:
    # Mock sys.argv to simulate too few argumets using MonkeyPatch
    pytest.MonkeyPatch().setattr(sys, "argv", ["pizza.py"])

    with pytest.raises(SystemExit) as e:
        check_command_line_args()
    assert str(e.value) == "Too few command-line arguments"


def test_check_command_line_args_too_many_args() -> None:
    pytest.MonkeyPatch().setattr(sys, "argv", ["pizza.py", "hello.py", "goodbye.py"])

    with pytest.raises(SystemExit) as e:
        check_command_line_args()
    assert str(e.value) == "Too many command-line arguments"


def test_check_file_is_csv_file_not_csv_file() -> None:
    with pytest.raises(SystemExit) as e:
        check_file_is_csv_file("invalid_extension.txt")
    assert str(e.value) == "Not a CSV file"


def test_read_csv_as_dict() -> None:
    fake_csv = "name,age\nAlice,30\nBob,25\n"

    with patch("builtins.open", mock_open(read_data=fake_csv)):
        result = read_csv_as_dict("dummy.csv")

    assert result == {"name": ["Alice", "Bob"], "age": ["30", "25"]}


def test_read_csv_as_dict_no_headers() -> None:
    fake_csv = ""

    with patch("builtins.open", mock_open(read_data=fake_csv)):
        with pytest.raises(SystemExit) as e:
            read_csv_as_dict("dummy.csv")
        assert str(e.value) == "Error: Could not find CSV headers"


def test_read_csv_as_dict_csv_empty() -> None:
    fake_csv = "name,age"

    with patch("builtins.open", mock_open(read_data=fake_csv)):
        with pytest.raises(SystemExit) as e:
            read_csv_as_dict("dummy.csv")
        assert str(e.value) == "Error: CSV file is empty"
