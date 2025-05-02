s = "Anupama"
s_lower = s.lower()  
for i in s:
    if s_lower.count(i) == 1:
        print("First non-repeating character:", i)
        break
else:
    print("No non-repeating character found.")