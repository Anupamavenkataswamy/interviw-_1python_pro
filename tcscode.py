l1=[5,6,7,0,3,5,8,0]
l2=[]
l3=[]
for i in l1:
       if i!=0:
        l2.append(i)
       else:
          l3.append(i)
print(l2)
print(l3)
l2.extend(l3)
print(l2)
