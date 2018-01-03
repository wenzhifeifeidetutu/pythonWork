players = ['charles', 'martina', 'michael', 'eli']


for player in players[:]:
	print(player)

print('\n')

for player in players[1:3]:
	print(player)


bk_players = players
bk_players2 = players[:]

bk_players.pop()


print(bk_players)

print(players)



print(bk_players2)
