a=[]
n=int(input('enter the elements'))
for i in range(1,n+1):
	#print(i)
	b=int(input('entr the value'))
	a.append(b)
a.sort()
print('largest element:',a[n-1])	

