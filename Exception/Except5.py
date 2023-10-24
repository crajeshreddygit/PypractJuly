# default except block
try:
    x = int(input("Enter x value"))
    y = int(input("Enter y value"))
    print("Result :",x/y)

except:
    print("Please provide valid inputs")
