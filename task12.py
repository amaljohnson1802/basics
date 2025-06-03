a=int(input("enter the number:"))
total=0
for x in range(1,a):
    if a%x==0:
        total=total+x
if total==a:
    print(f"{a} is a perfect number")
else:
    print(f"{a} not a perfect number")