import math_tools

a = float(input("Please enter value for a:"))

b = float(input("Please enter value for b:"))


operation = input("Please enter which operation to perform: add, subtract, multiply, or divide:")


#mapping time!

operations = {
    "add": math_tools.add,
    "subtract": math_tools.subtract,
    "multiply": math_tools.multiply,
    "divide": math_tools.divide
}

#need to call functions

if operation in operations:
    answer = operations[operation](a, b)
    print("Answer:", answer)
else:
    print("This is not a valid operation")
