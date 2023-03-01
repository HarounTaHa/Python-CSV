import csv
import pathlib

path = pathlib.Path()
file = open(pathlib.Path(path.absolute(), 'employees.csv'), 'a', newline='')
dict_writer = csv.DictWriter(file, ['EMPLOYEE_ID','FIRST_NAME','LAST_NAME','EMAIL','PHONE_NUMBER'],delimiter=';')
# if you want to write header from csv.DictWriter use
# dict_writer.writeheader()
dict_writer.writerow(
    {'EMPLOYEE_ID': 203, 'FIRST_NAME': 'kalleb', "LAST_NAME": 'taha', "EMAIL": "h@h.sa", "PHONE_NUMBER": "+8215815061"})
file.close()