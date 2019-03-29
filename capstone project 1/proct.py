class Student():
	 # def __init__(self,Student_name,usn,ph_no,branch,marks):
	 # 	self.student_name=student_name
	 # 	self.usn=usn
	 # 	self.ph_no=(ph_no)
	 # 	self.branch=branch
	 # 	#self.pin=int(pin)
	 # 	self.marks={"internal":[],"external":[]}
	dictionary={}

	def studentdetails(self):
		#dictionary={}
		self.student_name=input('Enter name:')
		self.usn=input('Enter usn')
		self.ph_no=int(input('ph_no'))
		self.branch=input('enter branch')
		d = {}
		d["student_name"] = self.student_name
		d['ph_no']=self.ph_no
		d['branch']=self.branch

		self.dictionary[self.usn]= d

	def display_student_details(self):
		print('enter the usn')
		print(self.dictionary[self.usn])
		

	def enter_marks(self):
		self.marks={}
		#self.internals=[]
		#for i in range(3):
		internal=int(input('enter the marks:'))
			#self.inernals.append(internal)
		#print(self.internals)	
		self.marks['internal']=internals
		external=int(input('external marks:')) 	
		self.marks['external']=external

	def see_marks(self):
		print(self.marks)

if __name__ == "__main__":
	student=Student()
	student.studentdetails()
	student.display_student_details()
	student.enter_marks()
	student.see_marks()


 

		

				
		
