# Leap Year Challenge
# A normal year has 365 days, leap years have 366 days
# Condition 1 on every year that is evenly divisible by 4
# Condition 2: except every year that is evenly divisible by 100
# Condition 3: unless the years is also evenly divisible by 400


print("Welcome to the Leap Year Checking Application\n")
checkYear = float(input("Please input the year that you want to check: "))

# div_by_four = checkYear % 4
# div_by_hundred = checkYear % 100
# div_by_fourhundred = checkYear % 400

if checkYear % 4 != 0 :
    print("This is not a leap year!")
elif checkYear % 100 != 0:
    print("This is a leap year!")
elif checkYear % 400 != 0:
    print("This is not leap year!")
else:
    print("Your input is a leap year!")

