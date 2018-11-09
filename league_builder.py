import csv


def add_player(player):
	# open file
	file = open('teams.txt', 'a')
	# write player to file
	file.write(player)
	# close file
	file.close()


def organize_players():
	with open('soccer_players.csv', newline='') as csvfile:
		player_reader = csv.DictReader(csvfile, delimiter=',')
		rows = list(player_reader)
		for row in rows:
			if row['Soccer Experience'] == 'YES':
				player_yes = row['Name'] + ', ' + row['Soccer Experience'] + ', ' + row['Guardian Name(s)'] + '\n'
			else:
				player_no = row['Name'] + ', ' + row['Soccer Experience'] + ', ' + row['Guardian Name(s)']
		add_player(player_yes)
		add_player(player_no)
	
organize_players()
			

