a=int(input("Enter the size of the array: "))
print("Enter the elements:")
list1=[]
for x in range(a):
    n=int(input())
    list1.append(n)

l=[]
for i in list1:
    count=0
    for j in list1:
        if i>j:
            count=count+1
    l.append(count)
print(l)