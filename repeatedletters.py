A=raw_input()
p=len(A)
count=0
count1=0
AA=0

for i in range(0,p):
	count=0
	for k in range(0,p):
		if(A[i]==A[k]):
			count=count+1
	if(count1==0):
		count1=count
		AA=A[i]
	if(count1<count):
		count1=count
		AA=A[i]
print(AA)
