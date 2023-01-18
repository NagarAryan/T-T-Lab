year = int(input("Enter the year "))
if (year % 400 == 0) and (year % 100==0):
    print("It is a Leap year")
elif (year % 4 == 0) and (year % 100 !=0):
    print("It is a Leap year")
else:
    print("Not a Leap Year")

