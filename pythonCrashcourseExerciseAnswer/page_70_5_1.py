#if text 5-1

car = ['bmw', 'audi', 'benz', 'tex']

if 'aa' in car:
	print("aa is in my love car list ")

else:
	print(car)


test_car = 'bmw'
test_car1 = 'mm'

if test_car == car[0]:
	print("u are right "+ test_car)

test_car2 = 'BMW'

if test_car2.lower() == car[0] and test_car1 in car:
	print("test_car2.lower is in my love car"+test_car2+ " " + test_car1)

if test_car2.lower() == car[0] or test_car1 in car:
	print("test_car2.lower is in my love car"+test_car2+ " " + test_car1)