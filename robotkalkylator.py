#UPPGIFT 6

class Product(object):
	def __init__(self, price, count, vat):
		self.price = price
		self.count = count
		self.vat = vat

	def price_with_vat(self):
		return self.price * self.count * self.vat

robot = Product(price = 900, count = 2, vat = 1.25)

book = Product(price = 100, count = 1, vat = 1.06)

print(robot.price_with_vat() + book.price_with_vat())


#UPPGIFT 7

class Product(object):
	def __init__(self, price, count, vat):
		self.price = price
		self.count = count
		self.vat = vat

	def price_with_vat(self):
		return self.price * self.count * self.vat

products = [Product(price = 900, count = 2, vat = 1.25), Product(price = 100, count = 1, vat = 1.06)]
total_price = products[0].price_with_vat() + products[1].price_with_vat()

print(total_price)


#UPPGIFT 8

class Product(object):
	def __init__(self, price, count, vat):
		self.price = price
		self.count = count
		self.vat = vat

	def price_with_vat(self):
		return self.price * self.count * self.vat

# 0=robotar, 1=boken 
products = [Product(price = 900, count = 2, vat = 1.25), Product(price = 100, count = 1, vat = 1.06)]
total_price = 0

for all_elements in products:
	total_price += all_elements.price_with_vat()

print(total_price)

#UPPGIFT 9

class Product(object):
	def __init__(self, price, count, vat):
		self.price = price
		self.count = count
		self.vat = vat

	def price_with_vat(self):
		total = self.price * self.count * self.vat
		if self.price > 500:
			return 0.9 * total
		else:
			return total

# 0=robotar, 1=boken 
products = [Product(price = 900, count = 2, vat = 1.25), Product(price = 100, count = 1, vat = 1.06)]
total_price = 0

for all_elements in products:
	total_price += all_elements.price_with_vat()

print(total_price)
