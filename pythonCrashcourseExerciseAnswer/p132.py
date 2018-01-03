def make_sandwish( *ingredients):
	for ingredient in ingredients:
		print("add "+ ingredient)


make_sandwish('asdsadas', 'seafood', 'jijiji')
make_sandwish('asdas')
make_sandwish()


def build_profile(firstName, lastName, **user_info):
	""" 创建一个字典，其中包含我们知道的有关于用户的一切 """
	profile = {}
	profile['first_name'] = firstName
	profile['last_name'] = lastName
	for key, value in user_info.items():
		profile[key] = value

	return profile



my_profile = build_profile('wen', 'zhi', location='hubei', field = 'computer' )
	#传入key-value时候必须用key = value 
print(my_profile)


def build_car(manufacturer, model, **car_info):
	car_profile = {}
	car_profile['manufacturer'] = manufacturer
	car_profile['model'] = model
	for key, value in car_info.items():
		car_profile[key] = value

	return car_profile


car = build_car('subaru', 'outbak', color ='blue', tow_pakage = 'True')

print(car)