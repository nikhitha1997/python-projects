usn=[1,2,3]
names=['ramesh','suresh','andy']
database={}
j='0'
for i in usn:
	#for j in names:
	if j>=len(names):
		break
		database[i]=names[j]
		j=j+1
print(database)