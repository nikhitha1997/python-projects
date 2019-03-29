from bankmain import Account_maneger
account={}
account_no=1001
print('_'*50)
print('welcome to iron bank')
while True:
	print('hey what would u like todo today?\n\n\
		1.creat Account\n\
		2.check balance\n\
		4.withdraw ammount\n\
		5.exit\n')
	choice=int(input('enter account name:'))
	if choice==1:
		account_name=('enter account name:')
		balance=input('enter the opening balance:')
		pin=int(input('enter a pin for ur account:'))
		
