def main():
	score = 0
	scorelow = 0
	print("\n\tWelcome to: Luna\nThe space pirate adventure game\n\n\n")
	home = 'home'
	while home != "quit":
		home = input(f'Type "quit" to quit the game\nType "start" to start the game\nType "leaderboard" to see the leaderboard\n')
		if home == "start":
			print(f"Welcome to the luna")
			break
		if home == "leaderboard":
			print(f"\tLeaderboard:\nTop score:{score}\nLowest score:{scorelow}\n")
