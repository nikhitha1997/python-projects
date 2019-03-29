class Account_maneger:
	def __init__(self,account_name,account_no,balance,pin):
		self.account_name=account_name
		self.account_no=account_no
		self.balance=balance
		self.pin=pin
		self.transaction=[]

	def deposit(self,ammount):
		if ammount>1000:
			print('unable to deposit.please try again')
		elif ammount<0:
			print('invalid deposit ammount.try again')
		else:
			self.balance+=ammount
			print('ammount',self.balance)
			transaction=('+'+str(ammount),self.balance)
			self.transaction.append(transaction)

	
	def withdraw(self,ammount):

		if (self.balance-ammount:
			print('insuffician balance:')
		else:
		self.balance-=ammount
		print('ammmount:',self.balance)
		

	def show_balance(self):	
		print('total balance':self.balance)

	def account_statement(self):
		


		