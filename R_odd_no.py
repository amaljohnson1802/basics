a=[1,2,3,4,5,6,7,8,9,10]
for x in range(len(a)):
    if a[x]%2!=0:
        a[x]="&"

print(a[::-1])
