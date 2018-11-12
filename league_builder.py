import csv


# function to add player to separate file teams.txt
def add_player(name):
	# open file
	file = open('teams.txt', 'a')
	# write player to file
	file.write(name + '\n')
	# close file
	file.close()


def sharks_create():
	# read csv file with player information
	with open('soccer_players.csv', newline='') as csvfile:
		# store player information in a variable
		player_list = csv.DictReader(csvfile, delimiter=',')
		# convert player info into a list to be iterated through
		players = list(player_list)
		# iterate (PORTION of) list...
		for player in players[:3]:
			# if player is a YES to having soccer experience,
			if player['Soccer Experience'] == 'YES':
				# concatenate desired player info and write it to file using add_player
				add_player(player['Name'] + ', ' + player['Soccer Experience'] + ', ' + player['Guardian Name(s)'])
		for player in players[:6]:
			if player['Soccer Experience'] == 'NO':
				# concatenate desired player info and write it to file using add_player
				add_player(player['Name'] + ', ' + player['Soccer Experience'] + ', ' + player['Guardian Name(s)'])


def sharks_note():
	shark_practice = "Saturday at 9:00am"
	# read csv file with player information
	with open('soccer_players.csv', newline='') as csvfile:
		player_list = csv.DictReader(csvfile, delimiter=',')
		players = list(player_list)
		for player in players[:6]:
			player_name = to_snake_case(player['Name'])
			file = open('{}.txt'.format(player_name), 'a')
			file.write('Dear ' + player['Guardian Name(s)'] + ',\nYour child, ' + player['Name'] + ', has their first practice on ' + shark_practice + '. Thanks for joining our soccer league!')


def raptors_create():
	# read csv file with player information
	with open('soccer_players.csv', newline='') as csvfile:
		# store player information in a variable
		player_list = csv.DictReader(csvfile, delimiter=',')
		# convert player info into a list to be iterated through
		players = list(player_list)
		# iterate (PORTION of) list...
		for player in players[6:13]:
			# if player is a YES to having soccer experience,
			if player['Soccer Experience'] == 'YES':
				# concatenate desired player info and write it to file using add_player
				add_player(player['Name'] + ', ' + player['Soccer Experience'] + ', ' + player['Guardian Name(s)'])
		for player in players[6:11]:
			if player['Soccer Experience'] == 'NO':
				# concatenate desired player info and write it to file using add_player
				add_player(player['Name'] + ', ' + player['Soccer Experience'] + ', ' + player['Guardian Name(s)'])


def raptors_note():
	raptor_practice = "Saturday at 10:00am"
	# read csv file with player information
	with open('soccer_players.csv', newline='') as csvfile:
		player_list = csv.DictReader(csvfile, delimiter=',')
		players = list(player_list)
		for player in players[6:11]:
			player_name = to_snake_case(player['Name'])
			file = open('{}.txt'.format(player_name), 'a')
			file.write('Dear ' + player['Guardian Name(s)'] + ',\nYour child, ' + player['Name'] + ', has their first practice on ' + raptor_practice + '. Thanks for joining our soccer league!')
		for player in players[12:13]:
			player_name = to_snake_case(player['Name'])
			file = open('{}.txt'.format(player_name), 'a')
			file.write('Dear ' + player['Guardian Name(s)'] + ',\nYour child, ' + player['Name'] + ', has their first practice on ' + raptor_practice + '. Thanks for joining our soccer league!')


def dragons_create():
	# read csv file with player information
	with open('soccer_players.csv', newline='') as csvfile:
		# store player information in a variable
		player_list = csv.DictReader(csvfile, delimiter=',')
		# convert player info into a list to be iterated through
		players = list(player_list)
		# iterate (PORTION of) list...
		for player in players[13:]:
			# if player is a YES to having soccer experience,
			if player['Soccer Experience'] == 'YES':
				# concatenate desired player info and write it to file using add_player
				add_player(player['Name'] + ', ' + player['Soccer Experience'] + ', ' + player['Guardian Name(s)'])
		for player in players[11:]:
			if player['Soccer Experience'] == 'NO':
				# concatenate desired player info and write it to file using add_player
				add_player(player['Name'] + ', ' + player['Soccer Experience'] + ', ' + player['Guardian Name(s)'])


def dragons_note():
	dragon_practice = "Saturday at 11:00am"
	# read csv file with player information
	with open('soccer_players.csv', newline='') as csvfile:
		player_list = csv.DictReader(csvfile, delimiter=',')
		players = list(player_list)
		for player in players[11:12]:
			player_name = to_snake_case(player['Name'])
			file = open('{}.txt'.format(player_name), 'a')
			file.write('Dear ' + player['Guardian Name(s)'] + ',\nYour child, ' + player['Name'] + ', has their first practice on ' + dragon_practice + '. Thanks for joining our soccer league!')
		for player in players[14:]:
			player_name = to_snake_case(player['Name'])
			file = open('{}.txt'.format(player_name), 'a')
			file.write('Dear ' + player['Guardian Name(s)'] + ',\nYour child, ' + player['Name'] + ', has their first practice on ' + dragon_practice + '. Thanks for joining our soccer league!')


# function to create team name and insert in teams.txt
def create_team(team):
	file = open('teams.txt', 'a')
	file.write(team + '\n')


# function to convert player name to lower and snake_case for title of 'Welcome' letters
def to_snake_case(name):
	final = ''
	for i in range(len(name)):
		item = name[i]
		if i < len(name) - 1:
			next_char_will_be_underscored = name[i+1] == '_' or name[i+1] == ' ' or name[i+1].isupper()
		if (item == ' ' or item == '_') and next_char_will_be_underscored:
			continue
		elif item == ' ' or item == '_':
			final += "_"
		elif item.isupper():
			final += '_'+item.lower()
		else:
			final += item
	if final[0] == '_':
		final = final[1:]
	return final

# to make sure script isn't executed when imported
if __name__ == '__main__':
	create_team('Sharks')
	sharks_create()
	sharks_note()
	create_team('Raptors')
	raptors_create()
	raptors_note()
	create_team('Dragons')
	dragons_create()
	dragons_note()
