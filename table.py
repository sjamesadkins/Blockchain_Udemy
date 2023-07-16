
from tabulate import tabulate

data = [
    ["Date", "Transaction", "Amount", "Category"],
    ["6/12/2023", "Schnucks", 45.00, "Food"],
    ["6/13/2023", "Amazon", 12.00, "Supply"],
    ["6/14/2023", "Tik Tok Tavern", 24.00, "Entertainment"]
]


def sort_and_tabulate(d):

    sorted_data = sorted(d[1:], key=lambda row: row[0])  # Sort by date
    sorted_data.insert(0, data[0])
    table = tabulate(sorted_data, headers="firstrow", tablefmt="grid")
    return table


def add_transaction(a, b):
    updated_data = a.append(b)


new_data = ["6/13/2023", "Penzey's", 32.00, "Supply"]

add_transaction(data, new_data)
table = sort_and_tabulate(data)

new_data_23_6_13 = ["6/13/2023", "Rockwell Brewing", 12.00, "Entertainment"]

add_transaction(data, new_data_23_6_13)
table = sort_and_tabulate(data)

new_data_23_6_13_2 = ["6/13/2023", "Schnucks", 50.00, "Food"]

add_transaction(data, new_data_23_6_13_2)
table = sort_and_tabulate(data)



print(table)

