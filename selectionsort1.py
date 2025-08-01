mylist =[90,34,23,12,10,20,45]

length = len(mylist)
for i in range(length):
    for j in range(i+1,length):
        if mylist[i] > mylist[j]:
            mylist[i],mylist[j] = mylist[j],mylist[i]
print(mylist)