import os
fn = input("Enter file to check")
if os.path.isfile(fn):
    print("File exists :",fn)
    f = open(fn,'r')
    data = f.read()
    print("* " * 20)
    print(data)
    print("* " * 20)
    f.close()
else:
    print("file not avilable")
