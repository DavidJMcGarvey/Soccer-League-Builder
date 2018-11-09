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
		# store player infomation in a variable
		player_list = csv.DictReader(csvfile, delimiter=',')
		# convert player info into a list to be iterated through
		rows = list(player_list)
		# iterate 
		for row in rows:
			# if player is a YES to having soccer experience,
			if row['Soccer Experience'] == 'YES':
				# get desired info, concatenate it, store it to variable
				add_player(row['Name'] + ', ' + row['Soccer Experience'] + ', ' + row['Guardian Name(s)'])
			else:
				pass


def no_ex_players():
	# read csv file with player information
	with open('soccer_players.csv', newline='') as csvfile:
		# store player infomation in a variable
		player_list = csv.DictReader(csvfile, delimiter=',')
		# convert player info into a list to be iterated through
		rows = list(player_list)
		# iterate
		for row in rows:
			# if player is a YES to having soccer experience,
			if row['Soccer Experience'] == 'NO':
				add_player(row['Name'] + ', ' + row['Soccer Experience'] + ', ' + row['Guardian Name(s)'])
			else:
				pass

yes_ex_players()
no_ex_players()
