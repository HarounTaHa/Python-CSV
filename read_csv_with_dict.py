import csv
import pathlib

path = pathlib.Path()
file = open(pathlib.Path(path.absolute(), 'employees.csv'))
dict_reader = csv.DictReader(file)
for row in dict_reader:
    print(row['FIRST_NAME'], row['LAST_NAME'], row['EMAIL'])
