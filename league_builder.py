import csv


# function to add player to separate file teams.txt
def add_player(name):
	# open file
	file = open('teams.txt', 'a')
	# write player to file
	file.write(name + '\n')
	# close file
	file.close()


# function to create team name and insert in teams.txt
def add_team_name(team):
	file = open('teams.txt', 'a')
	file.write(team + '\n')


def create_team(team):
	# read csv file with player information
	with open('soccer_players.csv', newline='') as csvfile:
		# store player information in a variable
		player_list = csv.DictReader(csvfile, delimiter=',')
		# convert player info into a list to be iterated through
		players = list(player_list)
		# iterate (PORTION of) list...
		if team == 'Sharks':
			create_note(team)
			add_team_name('Sharks')
			for player in players[:3]:
				# if player is a YES to having soccer experience,
				if player['Soccer Experience'] == 'YES':
					# concatenate desired player info and write it to file using add_player
					add_player(player['Name'] + ', ' + player['Soccer Experience'] + ', ' + player['Guardian Name(s)'])
			for player in players[:6]:
				if player['Soccer Experience'] == 'NO':
					# concatenate desired player info and write it to file using add_player
					add_player(player['Name'] + ', ' + player['Soccer Experience'] + ', ' + player['Guardian Name(s)'])
		if team == 'Raptors':
			create_note(team)
			add_team_name('Raptors')
			for player in players[6:13]:
				# if player is a YES to having soccer experience,
				if player['Soccer Experience'] == 'YES':
					# concatenate desired player info and write it to file using add_player
					add_player(player['Name'] + ', ' + player['Soccer Experience'] + ', ' + player['Guardian Name(s)'])
			for player in players[6:11]:
				if player['Soccer Experience'] == 'NO':
					# concatenate desired player info and write it to file using add_player
					add_player(player['Name'] + ', ' + player['Soccer Experience'] + ', ' + player['Guardian Name(s)'])
		if team == 'Dragons':
			create_note(team)
			add_team_name('Dragons')
			for player in players[13:]:
				# if player is a YES to having soccer experience,
				if player['Soccer Experience'] == 'YES':
					# concatenate desired player info and write it to file using add_player
					add_player(player['Name'] + ', ' + player['Soccer Experience'] + ', ' + player['Guardian Name(s)'])
			for player in players[11:]:
				if player['Soccer Experience'] == 'NO':
					# concatenate desired player info and write it to file using add_player
					add_player(player['Name'] + ', ' + player['Soccer Experience'] + ', ' + player['Guardian Name(s)'])


def create_note(team):
	shark_practice = "Saturday at 9:00am"
	raptor_practice = "Saturday at 10:00am"
	dragon_practice = "Saturday at 11:00am"
	# read csv file with player information
	with open('soccer_players.csv', newline='') as csvfile:
		player_list = csv.DictReader(csvfile, delimiter=',')
		# convert player info into a list to be iterated through
		players = list(player_list)
		# iterate (PORTION of) list...
		if team == 'Sharks':
			for player in players[:6]:
				# call function to convert player name to snake and lower cases
				player_name = to_snake_case(player['Name'])
				# open and create file per player name
				file = open('{}.txt'.format(player_name), 'a')
				# write message to that file with welcome message to guardian(s)
				file.write('Dear ' + player['Guardian Name(s)'] + ',\nYour child, ' + player['Name'] + ', has their first practice on ' + shark_practice + '. Thanks for joining our soccer league!')
		if team == 'Raptors':
			for player in players[6:11]:
				# call function to convert player name to snake and lower cases
				player_name = to_snake_case(player['Name'])
				# open and create file per player name
				file = open('{}.txt'.format(player_name), 'a')
				# write message to that file with welcome message to guardian(s)
				file.write('Dear ' + player['Guardian Name(s)'] + ',\nYour child, ' + player[
					'Name'] + ', has their first practice on ' + raptor_practice + '. Thanks for joining our soccer league!')
			# iterate (other PORTION of) list...
			for player in players[12:13]:
				# call function to convert player name to snake and lower cases
				player_name = to_snake_case(player['Name'])
				# open and create file per player name
				file = open('{}.txt'.format(player_name), 'a')
				# write message to that file with welcome message to guardian(s)
				file.write('Dear ' + player['Guardian Name(s)'] + ',\nYour child, ' + player[
					'Name'] + ', has their first practice on ' + raptor_practice + '. Thanks for joining our soccer league!')
		if team == 'Dragons':
			for player in players[11:12]:
				# call function to convert player name to snake and lower cases
				player_name = to_snake_case(player['Name'])
				# open and create file per player name
				file = open('{}.txt'.format(player_name), 'a')
				# write message to that file with welcome message to guardian(s)
				file.write('Dear ' + player['Guardian Name(s)'] + ',\nYour child, ' + player[
					'Name'] + ', has their first practice on ' + dragon_practice + '. Thanks for joining our soccer league!')
			# iterate (other PORTION of) list...
			for player in players[13:]:
				# call function to convert player name to snake and lower cases
				player_name = to_snake_case(player['Name'])
				# open and create file per player name
				file = open('{}.txt'.format(player_name), 'a')
				# write message to that file with welcome message to guardian(s)
				file.write('Dear ' + player['Guardian Name(s)'] + ',\nYour child, ' + player[
					'Name'] + ', has their first practice on ' + dragon_practice + '. Thanks for joining our soccer league!')
			
			
# function to convert name to snake and lower cases
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


def main():
	create_team('Sharks')
	create_team('Raptors')
	create_team('Dragons')


# to make sure script isn't executed when imported
if __name__ == '__main__':
	main()