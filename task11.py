a=int(input("enter the number:"))
b=str(a)
total=0
for x in b:
    total=total+(int(x)**3)
if total==a:
    print(f"{a} it is an amstrong")
else:
    print(f"{a} it is not an amstrong")
