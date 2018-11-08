import csv

with open('soccer_players.csv', newline='') as csvfile:
	player_reader = csv.DictReader(csvfile, delimiter=',')
	rows = list(player_reader)
	
	for row in rows[::]:
		if row['Soccer Experience'] == 'YES':
			player_yes = row
		elif row['Soccer Experience'] == 'NO':
			player_no = row['Soccer Experience']
	print(player_yes)
			

	def add_player(player):
		# open file
		file = open('teams.txt', 'a')
		# write player to file
		file.write(player['Guardian Name(s)'])
		# close file
	
add_player(player_yes)