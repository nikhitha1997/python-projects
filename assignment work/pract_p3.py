a={'a':'hellow','b':'hey','3':'hi'}
key=input()
value=input()
if key not in a:
	a[key]=value
print(a)