my_tuple=(1,3,6,8,9,10,7)
my_list=list(my_tuple)
first=my_list[0]
second=my_list[0]
for x in my_list:
    if first<x:
        second=first
        first=x
    elif second!=first and second<x:
        second=x
print("largest is",first)
print("second largest is",second)