try:
    print(10/0)
except ZeroDivisionError as msg:
    print("Exception : ",type(msg))
    print("Exception Type : ", msg.__class__)
    print("Except Class name : ", msg.__class__.__name__)
    print("Exception description : ",msg)

