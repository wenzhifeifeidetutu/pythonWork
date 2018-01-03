class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(self.restaurant_name)
		print(self.cuisine_type)

	def open_restaurant(self):
		msg = "restaurant is open"
		print(msg)

	def set_number_served(self, change_served):
		self.number_served = change_served

	def increment_number_served(self, add_number):
		self.number_served += add_number

restaurant = Restaurant('feizai'.title(),  'chongqingcai'.title())
print(restaurant.restaurant_name + " "+ restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


restaurant1 = Restaurant('pangzhi'.title(), 'shanghai'.title())
restaurant2 = Restaurant('souzhi'.title(), 'beijing'.title())
restaurant3 = Restaurant('jizhi'.title(), 'hh'.title())

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

restaurant1.set_number_served(1000)
restaurant1.increment_number_served(100)

# print(str(restaurant1.number_served) ) 
