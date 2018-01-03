def show_magicians(magics):
	for magic in magics:
		print(magic)

magics = ['sss', 'pdd', 'wuwukai', ]


show_magicians(magics)

change_magics = []

def make_great(magics):
	while magics:
		magic = magics.pop()
		magic = "The Great "+ magic 
		change_magics.append(magic)

	for magic in change_magics:
		magics.append(magic)

print()

show_magicians(magics)

make_great(magics[:])

show_magicians(magics)

make_great(magics)

show_magicians(magics)

