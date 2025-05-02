for num in range(100, 201):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        print(num,"is a prim number")
    else:
        print(num,"is a not prim nuber")
