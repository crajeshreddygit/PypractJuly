import csv
with open('emp.csv', 'r') as f :
    r = csv.reader(f)
    data = list(r)
    for row in data :
        for col in row :
            print(col, '\t', end = '')
        print()


