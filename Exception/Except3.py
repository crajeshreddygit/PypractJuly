try:
    x = int(input("Enter x value"))
    y = int(input("Enter y value"))
    print("Result :",x/y)
except BaseException as msg:
    print("Exception type :",type(msg))
    print("Exception Type : ", msg.__class__)
    print("Except Class name : ", msg.__class__.__name__)
    print("Exception description : ",msg)
