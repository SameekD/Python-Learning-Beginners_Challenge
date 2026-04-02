num1 = int(input("Enter first number to compare :"))
num2 = int(input("Enter second number to compare :"))
num3 = int(input("Enter third number to compare :"))

if num1 > num2 & num1 > num3 :
    print(f"{num1} is greater than both {num2} and {num3}.")
elif num2 > num1 & num2 > num3 :
        print(f"{num2} is greater than both {num1} and {num3}.")
else:
    print(f"{num3} is greater than both {num1} and {num2}.")