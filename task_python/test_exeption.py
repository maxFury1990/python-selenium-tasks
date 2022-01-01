
numbers = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten"
          ]


class FatalException(Exception):
    """Raise for my specific kind of exception"""


def parse_method(string_number):
    if string_number not in numbers:
        raise FatalException('Invalid data')


def test_parse_method_valid():
    parse_method("three")


def test_parse_method_invalid_with_int():
    parse_method("14")


def test_parse_method_invalid_with_data():
    parse_method("string")
