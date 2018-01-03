def favorite_book(title):
	print("One of my favorite books is " + title)


favorite_book('Alice in wonderland')



def make_shirt(closh_size, closh_type ):
	print("closh_size: " + closh_size + ", closh_type: " + closh_type)


make_shirt('M', 'I love python ')


def make_shirt_L(closh_size = 'L', closh_type = 'I love Python'):
	print("closh_size: " + closh_size + "closh_type : "+ closh_type)


make_shirt_L()


def describe_city(city_name, city_country = 'china'):
	print("city_name : "+ city_name.title() + " city_country: "+ city_country.title())

describe_city('wuhan')
describe_city('shanghai', 'china')
describe_city('Reykjavik', 'Iceland')