s="Test123@"
letter=0
number=0
spe=0
for i in s:
    if i.isalpha():
        letter+=1
    elif i.isdigit():
        number+=1
    else:
        spe+=1
print('letter: ' ,letter)
print('number: ' ,number)
print('special:' ,spe)