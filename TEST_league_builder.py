import csv


all_players = []
experienced_players = []
novice_players = []
Dragons = []
Raptors = []
Sharks = []


def read_csv(csv_file):
	with open(csv_file, 'r') as file:
		rows = csv.reader(file)
		for row in rows:
			all_players.append(row)


def create_team():
	for player in all_players:
		if player[2] == 'YES':
			experienced_players.append(player)
		if player[2] == 'NO':
			novice_players

read_csv("Soccer_players.csv")
create_team()
print(experienced_players)
