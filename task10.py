a=int(input("enter the year:"))
if a%100!=0 and a%4==0:
    print(f"{a} is a leap year")
else:
    print(f"{a} not a leap year")