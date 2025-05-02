s="Madam"
s1 = ''.join(i.lower() for i in s if i.isalpha)
if s1==s1[::-1]:
    print("yes, the string is palindrom")
else:
    print("no, the string is not a palindron")