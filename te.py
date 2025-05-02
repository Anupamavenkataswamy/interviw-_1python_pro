s="I love Python"
sp=s.split()
rev_word=[i[::-1] for i in sp]
rev=" ".join(rev_word)
print(rev)