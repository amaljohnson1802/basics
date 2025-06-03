my_tuple=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)
my_list=list(my_tuple)
for x in range(len(my_list)):
    if my_list[x]%7==0:
        my_list[x]="%"
    elif my_list[x]%2==0:
        my_list[x]="@"
my_tuple=tuple(my_list)
print(my_tuple)