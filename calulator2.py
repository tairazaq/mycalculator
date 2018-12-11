name = input("what is your name?")
number1_str = input("first number:")
number1 = int(number1_str)

number2_str = input("second number:")
number2 = int(number2_str)


operation = input("operation [+,-,*,/]:")

if operation == "+":
    combination = (number1) + (number2)
if operation == "-":
    combination = (number1) - (number2)
if operation == "*":
    combination = (number1) * (number2)
if operation == "/":
    combination = (number1) / (number2)
else:
    
    
 combination_str = str(combination)
print(name + " number is " + combination_str)
