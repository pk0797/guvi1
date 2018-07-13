num=input()
fact=1
if num<0:
	print("invalid input")
elif num==0:
	print("the factorial of 0 is 1")
else:
	for i in range(1,num+1):
		fact*=i
print("the factorial of ",num,"is",fact)
		
