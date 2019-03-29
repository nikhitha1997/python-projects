import csv
with open('event.csv','a',newline='')as myfile:
	csv_writer=csv.writer(myfile)
	csv_writer.writerow(['studen name','event',])
	#csv_writer.writerow(see_participant())
	
# with open('event.csv','r',newline='')as myfile:
# 	csv_reader=csv.reader(myfile)
# 	for i in csv_reader:
# 		print(i)	
		

