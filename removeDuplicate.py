l1=[1,2,4,1,5,37,2]
l2=[] #unique list
dup=[] #Duplicate List
for i in l1:
    if i not in l2:
        l2.append(i)
    else:
        dup.append(i)
print(l1)
print(dup)#Duplicate List
print(l2) #unique list