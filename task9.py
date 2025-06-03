a=int(input("enter the number:"))
if a==1:
    print("not prime")
else:
    for i in range(2,a):
        if a%i==0:
            print(f"{a}it is not a prime number")
            break
    else:
        print(f"{a}it is a prime number")