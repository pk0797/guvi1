import string
 
def ispangram(p, k=string.ascii_lowercase):
    k= set(k)
    return k <= set(p.lower())
 
if  ispangram(input())== True:
	print("yes")
else:
            print("no")
