class Point():
	"""docstring for point"""
	def __init__(self, x=0,y=0):
		self.x=x
		self.y=y
	def __add__(self,second):
		x=self.x-second.x
		y=self.y-second.y
		return Point(x,y) 
p1=Point(3,4)
p2=Point(1,2)
result=p1+p2
print(result.x,result.y)
#-----------------------------------	
# class A:
# 	def __init__(self,i=0):
# 		self.i=i
# class B(A):
# 	def __init__(self,j=0):
# 		self.j=j
# def main():
# 	b=B()
# 	print(b.i)
# 	print(b.j)
# main()					