p=raw_input()
k=['a','e','i','o','u']
l=list(p)
for i in l:
    if i in k:
        l.remove(i)
l=(l[::-1])
l="".join(l)
print(l)
