import logging

logging.basicConfig(filename='LE1.txt',level=40,filemode='w' , format='%(asctime)s:%(levelname)s:%(msg)s',datefmt='%d/%m/%Y %I:%M:%S %p')

logging.info("A new request came")
try:
    x = int(input("Enter x value"))
    y = int(input("Enter y value"))
    print("Result of x/y i :",x/y)
except ZeroDivisionError as msg:
    print("Can not divide with zero")
    logging.exception(msg)

except ValueError as msg:
    print("Please provide int values only")
    logging.exception(msg)

else:
    logging.info("Request processing completed successfully")

