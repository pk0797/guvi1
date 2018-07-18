num=int(input())
p=[]
k=2
while(num!=1):
	if num%k==0:
		num=num//k
		p.append(k)
		print(num)
		k=2
	else:
		k=k+1
ans=''
for k in p:
	ans=ans+" "+str(k)
print("The ans is:",ans)
