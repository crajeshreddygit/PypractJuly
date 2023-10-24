import csv
with open('emp.csv', 'w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['EmpName', 'Salary'])
    while True:
        name = input("enter name :")
        sal = float(input("enter salary:"))
        w.writerow([name, sal])
        opt = input("Do u want to add more Y/N?")
        if opt.lower() == 'no' :
            break ;
    f.close()


