# a=[1,2,3,4]
# mul=1
# for num in a:
# 	mul=mul*num
# 	print(mul)
a={1:'speckbit',2:'world',3:'quiet'}
for key,value in a.items():
	search_val=input('search:')
	if search_val==value:
		print('true')
	else:
		print('false')	