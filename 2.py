import csv


with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        value_from_col1 = row[0]
        value_from_col2 = row[1]
        print(value_from_col1, value_from_col2)