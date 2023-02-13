def main():
	score = 0
	scorelow = 0
	print("\n\tWelcome to: Luna\nThe space pirate adventure game\n\n\n")
	home = 'home'
	while home != "quit":
		home = input(f'Type "quit" to quit the game\nType "start" to start the game\nType "leaderboard" to see the leaderboard\n')
		if home == "start":
			print(f"\nWelcome to the luna\n\n")
			print(f"Your adventure starts in a prison cell you apear to be in a spaceship prison.\nYou see other cells with nobody in them and a gaurd asleep, holding a key.\nIt apears that the cell you are in is unlocked.")
			choice1 = input(f'Type "leave" to leave the cell and explore the ship, type "stay" to stay in your cell.\n')
			if choice1 == "leave":
				print(f'\nyou leave your cell and are standing in a hallway with a door at the end of it and multiple other cells.\nYou see the guard with a key, type "steal" to steal the key')
			elif choice1 == "stay":
				print(f"You stay in your prison cell")
			break
		if home == "leaderboard":
			print(f"\tLeaderboard:\nTop score:{score}\nLowest score:{scorelow}\n")
