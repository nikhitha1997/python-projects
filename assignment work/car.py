class vehicle():
	base_saleprice=0
	def __init__(self,model,wheel,sold_on):
		self.model=model
		self.wheel=wheel
		self.sold_on=sold_on
	def sale_price(self):
		if self.sold_on is not None:
			return 0.0
		return 5000.0*self.wheels



