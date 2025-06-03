i=1
# while i<=50:
b=int(input("enter the number:"))
for i in range(1,b):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
    # i=i+1