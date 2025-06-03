a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if a>b and a>c:
    print(f"{a}is largest number")
elif b>a and b>c:
    print(f"{b}is largest number")
else:
    print(f"{c}is largest number")