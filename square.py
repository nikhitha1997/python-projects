a=[1,2,1,3,4,64,35,93,35,87,4,3]
b=[]
for num in a:
	if num not in b:
		b.append(num)
print(b)			