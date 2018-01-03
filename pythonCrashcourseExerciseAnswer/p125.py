def city_country(city_name, city_country):
	msg =  city_name.title() +", "+ city_country.title()
	return msg

print(city_country('santiago', 'chile'))


def make_album(singer_name, album_name, music_number = ''):

	album_info = {'singer_name': singer_name, 'album_name': album_name, 'music_number'
		: music_number, }

	return album_info

print(make_album('liudehua'.title(), 'bingyu'.title(), '100'))


print(make_album('jiji'.title(), 'bingyu'.title(), '100'))


print(make_album('sadsa'.title(), 'bingyu'.title() ) )



while True:
	print("please input singer_name or album_name or music_number q to quit!")
	
	singer_name = input("singer_name: ")
	print(singer_name)

	if singer_name == 'q':
		break

	album_name = input("album_name: ")

	if album_name == 'q':
		break

	music_number = input("music_number: ")

	if music_number == 'q':
		break

album = make_album(singer_name, album_name, music_number)

print(album)