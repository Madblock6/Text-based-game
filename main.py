import random
def main():
	score = 0
	scorelow = 0
	choice1 = []
	decision = []
	decision = []
	decision = []
	decision = []
	decision = []
	decision = []
	decision = []
	decision = []
	guard2 = 5
	inventory = []
	Cafeteriadone = 0
	Weaponrydone = 0
	health = 20
	print("\n\tWelcome to: Luna\nThe space pirate adventure game\n\n\n")
	home = 'home'
	while home != "quit":
		home = input(f'Type "quit" to quit the game\nType "start" to start the game\nType "leaderboard" to see the leaderboard\n')
		if home == "start":
			print(f"\nWelcome to the luna\n\n")
			print(f"Your adventure starts in a prison cell, you apear to be in a spaceship prison.\nYou see other cells with nobody in them and a gaurd asleep, holding a key.\nIt apears that the cell you are in is unlocked.")
			while choice1 != "leave":
				choice1 = input(f'Type "leave" to leave the cell and explore the ship, type "stay" to stay in your cell.\n')
				if choice1 == "stay":
					print(f"You stay in your prison cell.")
			print(f'you leave your cell and are standing in a hallway with a door at the end of it and multiple other cells.')
			while decision != "steal":
				decision = input(f'You see the guard with a key, type "steal" to steal the key\n')
				if decision == "steal":
					print(f"You take the key.")
					inventory += ["Key"]
					print(f"Your inventory is now:")
					inv = ''
					for thing in inventory:
						inv += thing
					print(inv)
				else:
					print(f"unkown request")
			while decision != "exit":
				decision = input(f'If you would like to stay in the prison type "stay", if you would like to exit the prison type "exit".\n')
				if decision == "stay":
					print(f"You stay in the prison.")
				elif decision == "exit":
					continue
				else:
					print(f"unkown request")
			while decision != "elevator":
				if Weaponrydone == 1 and Cafeteriadone == 0:
					Cafeteriadone = 1
					print(f'You exit the armory and there is another room to the left with a sign that says cafeteria.')
					decision = input(f'Type "cafeteria" to enter the cafeteria.\n')
					if decision == "cafeteria":
						print(f'You enter the Cafeteria.\nYou see multiple different tables in a large room where there are many humans eating what might be their lunch.\nYou see a table with a man saying things to himself.\nYou also see a door in the corner with a sign that say Janitors closet.')
						while decision != "closet":
							decision = input(f'Type "talk" to talk to the man, type "closet" to search the closet.\n')
							if decision == "closet":
								print(f"You enter the closet and see multiple mops and cleaning supplies.\nYou see an ID with the name Diego on it and it says all access key.")
								inventory += ["Elevator key"]
								print(f"Your inventory is now:")
								print()
								inv = ''
								for thing in inventory:
									inv += f"{thing}\n"
								print(inv)
								print(f"You have nothing else to do in the cafeteria so you exit back to the hallway you were in.")
							elif decision == "talk":
								print(f'You go up to the man and he says:\n"You look lost, if you want to get out of here try to find an elevator key in the janitors closet."')
							else:
								print(f"unkown request")
				elif Cafeteriadone == 1 and Weaponrydone == 0:
					print(f'You exit the cafeteria and there is another room to the right with a sign that says weaponry.\n')
					decision = input(f'Type "weaponry" to enter the weaponry.\n')
					if decision == "weaponry":
						print(f"You enter the Weaponry.\nYou see a wall with 3 different guns on it, each gun has a different damage rating\nThe first gun you see is called a star blaster and does 2d6 damage.\nThe second gun you see is called a quantum rifle and does 1d12 damage.\nThe third and final guny you see is called a nebula shotgun and does 3d4 damage.")
						gundecision = input(f"Which gun do you choose?\n")
						Weaponrydone = 1
						if gundecision == "star blaster":
							print(f"You take the star blaster")
							inventory += ["star blaster"]
							print(f"Your inventory is now:")
							print()
							inv = ''
							for thing in inventory:
								inv += f"{thing}\n"
							print(inv)
						elif gundecision == "quantum rifle":
							inventory += ["quantum rifle"]
							print(f"You take the quantum rifle")
							print(f"Your inventory is now:")
							print()
							inv = ''
							for thing in inventory:
								inv += f"{thing}\n"
							print(inv)
						elif gundecision == "nebula shotgun":
							print(f"You take the nebula shotgun")
							inventory += ["nebula shotgun"]
							print(f"Your inventory is now:")
							print(inv)
							inv = ''
							for thing in inventory:
								inv += f"{thing}\n"
						else:
							print(f"unkown request")
				elif Cafeteriadone == 1 and Weaponrydone == 1:
					print(f"You have finished exploring all the rooms on the first floor.\nWhen you look into the hallway you see the security guard from earlier\nHe has a blaster drawn, he see's you and takes a shot\nWith a loud bang a blaster bolt hits you in the arm doing 4 points of damage\nYour health is now: {health-4}")
					decision = input(f'You take a look at the guard and point your gun\nType "shoot" to shoot at the guard\n')
					if decision == "shoot":
						print(f"You blast the security guard with your gun and he falls on the ground unconscious and leaves a path strait to the elevator.")
						decision = input(f'You walk up with the elevator key in your right hand\nType "elevator" to enter the elevator\n')
					else:
						print("unkown request")
				else:
					decision = input(f'You exit the Prison and in front of you there is an elevator, type "elevator" to go in\nTo the right you see a door with a sign that says weaponry, to the left you see a door with a sign that says cafeteria.\nType "weaponry" to go into the weaponry, type "cafeteria" to go into the cafeteria.\n')
					if decision == "elevator":
						if "Elevator key" in inventory:
							print(f"You go into the elevator")
						else:
							print(f"You do not have an elevator key to go in.")
							decision = "Nothing"
					elif decision == "weaponry":
						print(f"You enter the Weaponry.\nYou see a wall with 3 different guns on it, each gun has a different damage rating\nThe first gun you see is called a star blaster and does 2d6 damage.\nThe second gun you see is called a quantum rifle and does 1d12 damage.\nThe third and final gun you see is called a nebula shotgun and does 3d4 damage.")
						gundecision = input(f"Which gun do you choose?\n")
						Weaponrydone = 1
						if gundecision == "star blaster":
							print(f"You take the star blaster")
							inventory += ["star blaster"]
							print(f"Your inventory is now:")
							print()
							inv = ''
							for thing in inventory:
								inv += f"{thing}\n"
							print(inv)
						elif gundecision == "quantum rifle":
							inventory += ["quantum rifle"]
							print(f"You take the quantum rifle")
							print(f"Your inventory is now:")
							print()
							inv = ''
							for thing in inventory:
								inv += f"{thing}\n"
							print(inv)
						elif gundecision == "nebula shotgun":
							print(f"You take the nebula shotgun")
							inventory += ["nebula shotgun"]
							print(f"Your inventory is now:")
							print()
							inv = ''
							for thing in inventory:
								inv += f"{thing}\n"
							print(inv)
						else:
							print(f"unkown request")
					elif decision == "cafeteria":
						Cafeteriadone = 1
						print(f'You enter the Cafeteria.\nYou see multiple different tables in a large room where there are many humans eating what might be their lunch.\nYou see a table with a man saying things to himself.\nYou also see a door in the corner with a sign that say Janitors closet.')
						while decision != "closet":
							decision = input(f'Type "talk" to talk to the man, type "closet" to search the closet.\n')
							if decision == "closet":
								print(f"You enter the closet and see multiple mops and cleaning supplies.\nYou see an ID with the name Diego on it and it says all access key.")
								inventory += ["Elevator key"]
								print(f"Your inventory is now:")
								print()
								inv = ''
								for thing in inventory:
									inv += f"{thing}\n"
								print(inv)
								print(f"You have nothing else to do in the cafeteria so you exit back to the hallway you were in.")
							elif decision == "talk":
								print(f'You go up to the man and he says:\n"You look lost, if you want to get out of here try to find an elevator key in the janitors closet."')
							else:
								print(f"unkown request")
					else:
						print(f"unkown request")
			decision = ''
			while decision != "elevator":
				print(f'You step out onto the second floor of the ship and immediantly there are two guards at the doorway who grab you.\nOne of the guards says "where do you think youre going bucko?"\nAs they are carying you down a hall one of them slips on a banna peel somebody must have left on the floor.\nYou break free from the guards grip.')
				decision = input(f'You draw your blaster and look at the guard standing up.\nType "shoot" to shoot at the guard standing up.\n')
				while guard2 != 0:
					damage = 0
					if decision == 'shoot':
						if 'nebula shotgun' in inventory:
							for i in range(0, 3, 1):
								shot = random.randint(1, 4)
								damage += shot
							print(f"You pull out your nebula shotgun and do {damage} points of damage to the guard")
						elif 'quantum rifle' in inventory:
							for i in range(0, 1, 1):
								shot = random.randint(1, 12)
								damage += shot
							print(f"You pull out your quantum rifle and do {damage} points of damage to the guard")
						elif 'star blaster' in inventory:
							for i in range(0, 2, 1):
								shot = random.randint(1, 6)
								damage += shot
							print(f"You pull out your star blaster and do {damage} points of damage to the guard")
					guard2 -= damage
				print(f"Now that both guards are on the ground you can make a break for it back onto the elevator\nYou see the elevator door closing as you run towards it\nBefore you can get into the elevator the doors close and three more guards run up behind you.")

			break
		if home == "leaderboard":
			print(f"\tLeaderboard:\nTop score:{score}\nLowest score:{scorelow}\n")
		else:
			print(f"unkown request")
