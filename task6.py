a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=(input("enter the operator:"))
if c=="+":
    print(f"{a}+{b}={a+b}")
elif c=="-":
    print(f"{a}-{b}={a-b}")
elif c=="*":
    print(f"{a}*{b}={a*b}")
elif c=="/":
    print(f"{a}/{b}={a/b}")
else:
    print("operator not found")