import csv
import re


def convert(name):
	s1 = re.sub('(.)([A-Z][a-z])+', r'\1_\2', name)
	return re.sub('([a-z0-9])([A-Z])'), r'\1_\2', s1).lower()


# function to add player to separate file teams.txt
def add_player(player):
	# open file
	file = open('teams.txt', 'a')
	# write player to file
	file.write(player + '\n')
	# close file
	file.close()


def add_note_sharks():
	shark_practice = "Saturday at 9:00am"
	# raptor_practice = "Saturday at 10:00am"
	# dragon_practice = "Saturday at 11:00am"
	
	with open('soccer_players.csv', newline='') as csvfile:
		player_list = csv.DictReader(csvfile, delimiter=',')
		rows = list(player_list)
		for row in rows[:6]:
			file = open('{}.txt'.format(row['Name']), 'a')
			file.write('Dear ' + row['Name'] + ', ' + row['Guardian Name(s)'] + '. Your first practice is ' + shark_practice)


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


def create_raptors():
	# read csv file with player information
	with open('soccer_players.csv', newline='') as csvfile:
		# store player information in a variable
		player_list = csv.DictReader(csvfile, delimiter=',')
		# convert player info into a list to be iterated through
		rows = list(player_list)
		# iterate (PORTION OF) list
		for row in rows[6:13]:
			# if player is a YES to having soccer experience,
			if row['Soccer Experience'] == 'YES':
				# concatenate desired player info and write it to file using add_player
				add_player(row['Name'] + ', ' + row['Soccer Experience'] + ', ' + row['Guardian Name(s)'])
		for row in rows[9:12]:
			if row['Soccer Experience'] == 'NO':
				# concatenate desired player info and write it to file using add_player
				add_player(row['Name'] + ', ' + row['Soccer Experience'] + ', ' + row['Guardian Name(s)'])


def create_dragons():
	# read csv file with player information
	with open('soccer_players.csv', newline='') as csvfile:
		# store player information in a variable
		player_list = csv.DictReader(csvfile, delimiter=',')
		# convert player info into a list to be iterated through
		rows = list(player_list)
		# iterate list
		for row in rows[13:]:
			# if player is a YES to having soccer experience,
			if row['Soccer Experience'] == 'YES':
				# concatenate desired player info and write it to file using add_player
				add_player(row['Name'] + ', ' + row['Soccer Experience'] + ', ' + row['Guardian Name(s)'])
		for row in rows[13:]:
			if row['Soccer Experience'] == 'NO':
				# concatenate desired player info and write it to file using add_player
				add_player(row['Name'] + ', ' + row['Soccer Experience'] + ', ' + row['Guardian Name(s)'])


def create_team(team):
	file = open('teams.txt', 'a')
	file.write(team + '\n')


# Team names: Sharks, Raptors, Dragons
# !! How do I use the two functions that split the players into 3 teams?
# 3 players from each group (yes_ex and no_ex) per team
if __name__ == '__main__':
	convert(row['Name'])
	# create_team('Sharks')
	# create_sharks()
	# create_team('Raptors')
	# create_raptors()
	# create_team('Dragons')
	# create_raptors()
