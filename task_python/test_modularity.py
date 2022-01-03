from prettytable import PrettyTable


def test_csv():
    x = PrettyTable(["a", "b"])
    x.add_row([1, 2])
    print(x)