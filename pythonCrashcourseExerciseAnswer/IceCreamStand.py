from p142 import Restaurant

class IceCreamStand(Restaurant):
	def __init__(slef, restaurant_name, cuisine_type, flavors):
		super().__init__(restaurant_name, cuisine_type )
		slef.flavors = flavors


	def show_flavors(slef):
		for key, value in slef.flavors.items():
			print(key + " "+ value)





myIceCreamStand = IceCreamStand('jiji', 'ice', {'old':'nice_ice', 'yong':'cream_ice', 'boy':
	'jijiji'})
myIceCreamStand.show_flavors()
