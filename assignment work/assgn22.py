x={'key1':1,'key2':3,'key3':2}
y={'key1':1,'key2':2}
for i in x.items():
	for k in y.items():
		if i==k:
			print(f'{i} is present  both x and y')

	 