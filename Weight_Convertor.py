#weight Convertor

weight=float(input("Enter your Weight:\n"))
unit=input("Enter the unit,kilograms or Pounds:kg/L\n")
if unit=="kg":
    weight=weight*2.205
    unit="L"
    print(f"Your weight is {round(weight,1)}{unit}")
elif unit=='L':
    weight=weight/2.205
    unit="kg"
    print(f"Your weight is {round(weight,1)}{unit}")
else:
    print("Wrong unit")

