#n=int(input('enter the number'))
for n in range(1,100):
    sum = 0
    for i in range(1,n//2+1):
        if n%i==0:
            sum+=i
    if sum == n:
        print(n,"the number is perfect number")
    else:
        print(n,"the number is not a perfect number")
