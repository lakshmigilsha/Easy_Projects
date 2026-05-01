#Calculator
num1=int(input("Enter first number:\n"))
num2=int(input("Enter second number:\n"))
operation=input("choose operation:\nChoose A for multipliion\nchoose B for division\nchoose C for Addition\nchoose D for Subtraction\n")
if operation=='A':
    print(round(num1*num2,2))
elif operation=='B':
    print(round(num1/num2,2))
elif operation=='C':
    print(round(num1+num2))
elif operation=='D':
    print(round(num1-num2,2))
else:
    print("Wrong Operator")
