import csv


# function to add player to separate file teams.txt
def add_player(player):
	# open file
	file = open('teams.txt', 'a')
	# write player to file
	file.write(player+'\n')
	# close file
	file.close()


def yes_ex_players():
	# read csv file with player information
	with open('soccer_players.csv', newline='') as csvfile:
		# store player information in a variable
		player_list = csv.DictReader(csvfile, delimiter=',')
		# convert player info into a list to be iterated through
		rows = list(player_list)
		# iterate list
		for row in rows:
			# if player is a YES to having soccer experience,
			if row['Soccer Experience'] == 'YES':
				# concatenate desired player info and write it to file using add_player
				add_player(row['Name'] + ', ' + row['Soccer Experience'] + ', ' + row['Guardian Name(s)'])
			else:
				pass


def no_ex_players():
	# read csv file with player information
	with open('soccer_players.csv', newline='') as csvfile:
		# store player information in a variable
		player_list = csv.DictReader(csvfile, delimiter=',')
		# convert player info into a list to be iterated through
		rows = list(player_list)
		# iterate list
		for row in rows:
			# if player is a NO to having soccer experience,
			if row['Soccer Experience'] == 'NO':
				# concatenate desired player info and write it to file using add_player
				add_player(row['Name'] + ', ' + row['Soccer Experience'] + ', ' + row['Guardian Name(s)'])
			else:
				pass
			

def create_sharks():
	# read csv file with player information
	with open('soccer_players.csv', newline='') as csvfile:
		# store player information in a variable
		player_list = csv.DictReader(csvfile, delimiter=',')
		# convert player info into a list to be iterated through
		rows = list(player_list)
		# iterate list
		for row in rows[:3]:
			# if player is a YES to having soccer experience,
			if row['Soccer Experience'] == 'YES':
				# concatenate desired player info and write it to file using add_player
				add_player(row['Name'] + ', ' + row['Soccer Experience'] + ', ' + row['Guardian Name(s)'])
		for row in rows[:6]:
			if row['Soccer Experience'] == 'NO':
				# concatenate desired player info and write it to file using add_player
				add_player(row['Name'] + ', ' + row['Soccer Experience'] + ', ' + row['Guardian Name(s)'])
	


def create_team(team):
	file = open('teams.txt', 'a')
	file.write(team+'\n')

# Team names: Sharks, Raptors, Dragons
# !! How do I use the two functions that split the players into 3 teams?
# 3 players from each group (yes_ex and no_ex) per team
create_team('Sharks')
create_sharks()
