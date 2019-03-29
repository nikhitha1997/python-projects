event_details={'1':'cs 1.6','2':'google it','3':'treasurehunt'}
d={}

def add_participant():
	name=input('Enter name')
	event=input('Enter the serial number of teh event from the following list:\n\
	1.cs\n\
	2.google it\n\
	3.treasurehunt\n')
	d[name]=event
	see_participant()

def see_participant():
	for i,k in d.items():
		print(i,k,sep='-')

if __name__=='__main__':
	add_participant()
	print(d)
	see_participant()
	print()		
	



