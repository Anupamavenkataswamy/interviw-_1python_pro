a=input("enter the String")
b=input("enter the string")
if len(a)==len(b):
    if sorted(a)==sorted(b):
        print("the string is anagram")
    else:
        print("the string is not an anagram")
else:
    print("the strings are not anagram")
