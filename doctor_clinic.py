a=int(input("enter the no of patiens:"))
b=[]
f1=0
f2=0
f3=0
for x in range(a):
    age=int(input("enter the age:"))
    b.append(age)
for i in b:
    if i>0 and i<17:
        f1=f1+200
    elif i>=17 and i<=40:
        f2=f2+400
    elif i>40 and i<=120:
        f3=f3+300
    else:
        print("it is invalid")
print(f1+f2+f3)