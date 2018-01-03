people = {
	'first_name': 'Han',
	'last_name': 'jinglong',
	'age': 18,
	'city': 'beijing',

}

# print(people['first_name'])

# print(people['last_name'])

# print(str( people['age']) )

# print(people['city'])

for people_key, people_value in people.items():
	print("people_key: " + people_key)
	if isinstance(people_value, int):
		print("people_value: " +str(people_value))
	else:
		print("people_value: " + people_value)
# print(type(people['age']))

people['jiji'] = 'big jiji'

print(people)

del people['jiji']

print(people) 


user_o = {
	'username' :'efermi',
	'first' : 'enrico',
	'last' :'fermi',

}

for k, v in user_o.items():
	print("key "+ k)
	print("value "+ v)


rivers ={
	'nile':'egypt',
	'haunghe':'china',
	'long river':'china',

}

for river, nation in rivers.items():
	print("The " + river.title() + "runs through "+ nation.title())

for river in rivers.keys():
	print(river)

for nation in sorted(rivers.values()):
	print(nation)
