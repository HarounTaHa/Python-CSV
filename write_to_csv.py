import csv
import pathlib

# add multiple lines
header = ['EMPLOYEE_ID', 'FIRST_NAME', 'LAST_NAME', 'EMAIL', 'PHONE_NUMBER']
data = [
    ['198', 'Donald', 'OConnell', 'DOCONNEL', '650.507.9833'],
    ['199', 'Don', 'nell', 'aaa', '650.507.9833'],
    ['200', 'jemi', 'gabi', 'Dominix', '650.507.9833'],
    ['201', 'haroun', 'taha', 'gaza', '650.507.9833'],
    ['202', 'test', 'test', 'xx', '650.507.9833'],
]
path = pathlib.Path()
file = open(pathlib.Path(path.absolute(), 'employees.csv'), 'w', newline='')
writer = csv.writer(file)
# write one line
# writer.writerow(['206', 'Haroun', 'Taha', 'h@h.sa', '+970597818088'])
# write list data to csv and header
writer.writerow(header)
writer.writerows(data)
file.close()

# path = pathlib.Path()
# file = open(pathlib.Path(path.absolute(), 'employees.csv'), 'w', newline='')
# # delimiter and lineterminator keyword
# # delimiter use to separate data
# # lineterminator determine among lines
# writer = csv.writer(file, delimiter='\t', lineterminator='\n--------------------------\n')
# writer.writerow(['206', 'Haroun', 'Taha', 'h@h.sa', '+970597818088'])
# writer.writerow(['206', 'Ahmed', 'Taha', 'a@a.sa', '+970597779956'])
# writer.writerow(['206', 'Jamal', 'Taha', 'j@j.sa', '+970595828298'])
# file.close()