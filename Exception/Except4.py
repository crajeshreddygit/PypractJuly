try:
    x = int(input("Enter x value"))
    y = int(input("Enter y value"))
    print("Result :",x/y)

except (ArithmeticError, ValueError) as msg:
    print("Except Class name : ", msg.__class__.__name__)
    print("Exception description : ",msg)

