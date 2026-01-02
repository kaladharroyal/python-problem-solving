#creating calculator for addition, subtraction, multiplication and division
#input
num1 = int(input("enter the  number1: "))
num2 = int(input("enter the number2: "))
#process
operation = input("enter the operation you eant to perform: \n")
if operation == "=":
    print(f"the sum of {num1} and {num2} is {num1+num2}")
elif operation == "-":
    print(f"the difference of {num1}and {num2} is {num1-num2}")
elif operation =="*":
    print(f"the product of {num1} and {num2} is{num1*num2}")
elif operation == "/":
    if num2 == 0:
        print("division by zero not possible ")
    else:
        print(f"the division of {num1} and {num2} is {num1/num2}")
else:
    print("invalid operator is selected")