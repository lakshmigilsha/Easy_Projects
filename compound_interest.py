#Compound interest calculator

principal=0
rate=0
time=0

while principal<=0:
    principal=float(input("Enter the principal amount: "))
    if principal<=0:
        print("Enter a positive number for principal amount")

while rate<=0:
    rate=float(input("Enter the Interest rate: "))
    if rate<=0:
        print("Enter a positive rate value")

while time<=0:
    time=float(input("Enter the time period: "))
    if time<=0:
        print("Enter a positve time period")

total=principal*pow((1+rate/100),time)
print(f"Balance after {time}years is {total:.2f}")

