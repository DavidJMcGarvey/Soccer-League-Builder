import csv


# Empty lists for moving players around
all_players = []
experienced_players = []
novice_players = []
Dragons = []
Raptors = []
Sharks = []


def read_csv(csv_file):
	with open(csv_file, newline='') as file:
		rows = csv.reader(file, delimiter=',')
		for row in rows:
			all_players.append(row)


def experience_split():
	for player in all_players:
		if player[2] == 'YES':
			experienced_players.append(player)
		if player[2] == 'NO':
			novice_players.append(player)


def divide_teams(team):
	for player in experienced_players[:3]:
		if team == 'Sharks':
			Sharks.append(player)
			experienced_players.remove(player)
		if team == 'Raptors':
			Raptors.append(player)
			experienced_players.remove(player)
		if team == 'Dragons':
			Dragons.append(player)
			experienced_players.remove(player)
	for player in novice_players[:3]:
		if team == 'Sharks':
			Sharks.append(player)
			novice_players.remove(player)
		if team == 'Raptors':
			Raptors.append(player)
			novice_players.remove(player)
		if team == 'Dragons':
			Dragons.append(player)
			novice_players.remove(player)


# function to add teams to teams.txt
def add_team(team):
	with open('teams.txt', 'a') as file:
		file.write(team + '\n')
		if team == 'Sharks':
			for player in Sharks:
				player = player[0] + ', ' + player[2] + ', ' + player[3] + '\n'
				player = str(player)
				file.write(player)
		if team == 'Raptors':
			for player in Raptors:
				player = player[0] + ', ' + player[2] + ', ' + player[3] + '\n'
				player = str(player)
				file.write(player)
		if team == 'Dragons':
			for player in Dragons:
				player = player[0] + ', ' + player[2] + ', ' + player[3] + '\n'
				player = str(player)
				file.write(player)
	file.close()


def add_note(team):
	if team == 'Sharks':
		for player in Sharks:
			file = open('{}.txt'.format(player[0].lower().replace(' ', '_')), 'a')
			guardian = player[3]
			child = player[0]
			file.write("Dear " + guardian + ",\nWe're excited that your child, " + child + ", is joining the Sharks! Their first practice is this Saturday, 9:00am at Washington Park. We all are looking forward to a fun season!"  )
	if team == 'Raptors':
		for player in Raptors:
			file = open('{}.txt'.format(player[0].lower().replace(' ', '_')), 'a')
			guardian = player[3]
			child = player[0]
			file.write("Dear " + guardian + ",\nWe're excited that your child, " + child + ", is joining the Raptors! Their first practice is this Saturday, 10:00am at Washington Park. We all are looking forward to a fun season!"  )
	if team == 'Dragons':
		for player in Dragons:
			file = open('{}.txt'.format(player[0].lower().replace(' ', '_')), 'a')
			guardian = player[3]
			child = player[0]
			file.write("Dear " + guardian + ",\nWe're excited that your child, " + child + ", is joining the Dragons! Their first practice is this Saturday, 11:00am at Washington Park. We all are looking forward to a fun season!"  )


def main():
	read_csv("Soccer_players.csv")
	experience_split()
	divide_teams('Sharks')
	add_team('Sharks')
	add_note('Sharks')
	divide_teams('Raptors')
	add_team('Raptors')
	add_note('Raptors')
	divide_teams('Dragons')
	add_team('Dragons')
	add_note('Dragons')


if __name__ == '__main__':
	main()
