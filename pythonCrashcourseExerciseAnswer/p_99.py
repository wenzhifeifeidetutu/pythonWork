wenergou = {
	'first_name' : 'wen',
	'last_name' : 'zhi',
	'user_name': 'wenergou',
}

pdd = {
	'first_name':'liu',
	'last_name':'mou',
	'user_name':'liumou',

}

hanjinlong = {
	'first_name': 'han',
	'last_name': 'jinglong',
	'user_name':'hanjinlong',

}

peoples = [wenergou, pdd, hanjinlong]


for people in peoples:
	for namek, user_namev in people.items():
		print("namek: " + namek)
		print("user_namev:  "+ user_namev )




lily = {
	'type': 'cat',
	'muster_name': 'pdd',
}

jojo = {
	'type': 'dog',
	'muster_name': 'dashima',
}

jiji = {
	'type': 'fash',
	'muster_name': 'wenergou',
}

pets =[lily, jojo, jiji]

for pet in pets:
	print("muster_name "+pet['muster_name']+ " type "+  pet['type']+"\n " )





favorite_places = {
	'wenergou' : ['chongqing', 'chengdu', 'hangzou'],
	'pdd' : ['shanghai', 'wuhan'],
	'dashima': ['wanwu'],
}

for name in favorite_places.keys():
	print("name : " + name)
	for place in favorite_places[name]:
		print("palce: " + place)


number_like ={
	'wenergou': [1, 2, 4, 5, 6, 7, 8 ,9],
	'dashima': [1, 2, 3, 7],
	'pdd': [6, 6 ,6],

}

for name, number in number_like.items():
	print("name: " + name )
	for num in number:
		print(str(num))
 



