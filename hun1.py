    N=int(input())
    p=[]
    p=input().split()
    k=list()
    if(1<=N and N<=100000):
    	for i in range(N):
    		count=1
    		for j in range(i+1,N):
    			if(p[i]==p[j]):
    				count=count+1
    		#print("A[i]:",end=" "),print(A[i]),	print("count:",end=" "),print(count),print("B:",end=" "),print(B)
    		if(count>1 and int(p[i]) not in k):
    			k.append(int(p[i]))
    if(len(k)==0):
    	print("unique")
    else:
    	k.sort()		
    print(*k) 
