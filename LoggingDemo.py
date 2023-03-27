import logging
logging.basicConfig(filename='mylog27032023.log', level=logging.INFO, filemode='a',
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt="%d/%m/%Y %I:%M:%S %p")
logging.info("A new request came")
try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number : "))
    print("The division is : ", x/y)

except ZeroDivisionError as msg:
    print("Cannot divide by zero")
    logging.exception(msg)

except ValueError as msg:
    print("Invalid format of input")
    logging.exception(msg)

logging.info("Request processing complete")