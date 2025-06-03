a=[1,2,2,3,3,4,8,5,8,8,9,6,6,7,7]
b=[]
count=0
for x in a:
    if x not in b:
        b.append(x)
        count=count+1
print(f"count={count}")
print(b)