# def changeme( mylist ):
#    mylist.append([1,2,3,4]);
#    print("Values inside the function: ", mylist)
#    #print("Values outside the function: ", mylist)
#    return
# mylist = [10,20,30]
# changeme( mylist )
# print("Values outside the function: ", mylist)
#------------------------------------------------
# def add():
# 	a=20
# 	c=30
# 	print(a+c)
# 	return
# add()
#-----------------------------------------------------

# def student(name,usn):
# 	d=[]
# 	d.append(name)
# 	d.append(usn)
# 	print(d)
# name='hii'
# usn=23	
# student(name='nik',usn=63)
# student(name='hg',usn=63)
# print(name,usn)	
#------------------------------------------------------------
total = 0; # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print("Inside the function local total : ", total)
   return total

# Now you can call sum function
sum( 10, 20 )
print("Outside :",total)