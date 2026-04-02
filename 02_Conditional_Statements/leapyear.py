year = int(input("Enter a year to check if it's a leap year or not :"))
if (year % 4 == 0 & year % 100 != 0) or year % 400 == 0  :
    print(f"The year {year} is a leap year.")
else :
        print(f"The year {year} is not a leap year.")