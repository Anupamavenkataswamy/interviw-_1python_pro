n=int(input("enetr the number"))
l=int(len(str(n)))
sum=0
copy=n
while n>0:
    rem = n%10
    sum+=rem**l
    n=n//10
if copy==sum:
    print(copy,"is an amstrong nuber")
else:
    print(copy,"is not an amstrong number")