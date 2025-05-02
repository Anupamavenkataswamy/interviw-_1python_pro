l=[1,2,3,4,6,7,1,3,5,2,4,6,1,2,6,7]
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
        a=l.count(i)
        print(i,a)