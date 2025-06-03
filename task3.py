a=int(input("enter the marks:"))
if a<=100 and a>=90:
    print(f"{a} it is A grade")
elif a<=89 and a>=80:
    print(f"{a} it is B grade")
elif a<=79 and a>=70:
    print(f"{a} it is C grade")
elif a<=69 and a>=60:
    print(f"{a} it is D grade")
elif a<=59 and a>=50:
    print(f"{a} it is E grade")
elif a<=49:
    print("failed")
else:
    print(f"{a} invalid marks")