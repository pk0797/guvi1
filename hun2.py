N=int(input())
p=[]
p=input().split()
k=list()
if(1<=N and N<=100000):
	for i in range(N):
		k.append(int(p[i]))
while(k):
	print(max(k),end="")
	if(max(k)==0):
	   break
	else:
	   k.pop(k.index(max(k)))
