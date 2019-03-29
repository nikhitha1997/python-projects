import csv
# with open('file.csv','w',newline="") as myfile:
# 	wr = csv.writer(myfile, dialect='excel')
# 	wr.writerow(["hello",2])
with open('file.csv','r',newline="") as myfile:
	rd=csv.reader(myfile)
	# print(rd)
	for i in rd:
		#print(i[1])#to read 2nd column
		print(i)