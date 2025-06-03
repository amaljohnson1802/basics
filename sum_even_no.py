a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
b=[]
sum=0
for x in a:
    if x%2==0 and x%3==0:
        a.remove(x)
print(a)
for i in a:
    sum=sum+i
print(sum)
