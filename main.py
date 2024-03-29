import random
import pickle
def main():
	print("\n\tWelcome to: Luna\nThe space pirate adventure game\n\n\n")
	home = 'home'
	while home != "quit":
		home = input(f'Type "quit" to quit the game\nType "start" to start the game\nType "load" to load your game\n')
		if home == "start":
			print(f"\nWelcome to the luna\n\n")
			health = 20
			floor_1(health)
		elif home == "load":
			with open("pickles1.dat", "rb") as file:
				health = pickle.load(file)
				decision = pickle.load(file)
				inventory = pickle.load(file)
				room = pickle.load(file)
				if room == floor_2:
					floor_2(health, decision, inventory)
				if room == floor_3:
					floor_3(health, decision, inventory)
				if room == floor_4:
					floor_4(health, inventory, decision)
		else:
			print(f"unkown request")
def floor_1(health):
			decision = []
			inventory = []
			Weaponrydone = 0
			Cafeteriadone = 0
			print(f"Your adventure starts in a prison cell, you apear to be in a spaceship prison.\nYou see other cells with nobody in them and a gaurd asleep, holding a key.\nIt apears that the cell you are in is unlocked.")
			while decision != "leave":
				decision = input(f'Type "leave" to leave the cell and explore the ship, type "stay" to stay in your cell.\n').lower()
				if decision == "stay":
					print(f"You stay in your prison cell.")
			print(f'you leave your cell and are standing in a hallway with a door at the end of it and multiple other cells.')
			while decision != "steal":
				decision = input(f'You see the guard with a bag of chips, type "steal" to steal the bag of chips\n').lower()
				if decision == "steal":
					print(f"You take the key.")
					inventory += ["bag of chips"]
					print(f"Your inventory is now:")
					inv = ''
					for thing in inventory:
						inv += thing
					print(inv)
				else:
					print(f"unkown request")
			while decision != "exit":
				decision = input(f'If you would like to stay in the prison type "stay", if you would like to exit the prison type "exit".\n').lower()
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
					decision = input(f'Type "cafeteria" to enter the cafeteria.\n').lower()
					if decision == "cafeteria":
						print(f'You enter the Cafeteria.\nYou see multiple different tables in a large room where there are many humans eating what might be their lunch.\nYou see a table with a man saying things to himself.\nYou also see a door in the corner with a sign that say Janitors closet.')
						while decision != "closet":
							decision = input(f'Type "talk" to talk to the man, type "closet" to search the closet.\n').lower()
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
					decision = input(f'Type "weaponry" to enter the weaponry.\n').lower()
					if decision == "weaponry":
						print(f"You enter the Weaponry.\nYou see a wall with 3 different guns on it, each gun has a different damage rating\nThe first gun you see is called a star blaster and does 2d6 damage.\nThe second gun you see is called a quantum rifle and does 1d12 damage.\nThe third and final guny you see is called a nebula shotgun and does 3d4 damage.")
						gundecision = input(f"Which gun do you choose?\n").lower()
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
				elif Cafeteriadone == 1 and Weaponrydone == 1:
					print(f"You have finished exploring all the rooms on the first floor.\nWhen you look into the hallway you see the security guard from earlier\nHe has a blaster drawn, he see's you and takes a shot\nWith a loud bang a blaster bolt hits you in the arm doing 4 points of damage\nYour health is now: {health-4}")
					health = health - 4
					decision = input(f'You take a look at the guard and point your gun\nType "shoot" to shoot at the guard\n').lower()
					if decision == "shoot":
						print(f"You blast the security guard with your gun and he falls on the ground unconscious and leaves a path strait to the elevator.")
						decision = input(f'You walk up with the elevator key in your right hand\nType "elevator" to enter the elevator\n').lower()
					else:
						print("unkown request")
				else:
					decision = input(f'You exit the Prison and in front of you there is an elevator, type "elevator" to go in\nTo the right you see a door with a sign that says weaponry, to the left you see a door with a sign that says cafeteria.\nType "weaponry" to go into the weaponry, type "cafeteria" to go into the cafeteria.\n').lower()
					if decision == "elevator":
						if "Elevator key" in inventory:
							print(f"You go into the elevator")

						else:
							print(f"You do not have an elevator key to go in.")
							decision = "Nothing"
					elif decision == "weaponry":
						print(f"You enter the Weaponry.\nYou see a wall with 3 different guns on it, each gun has a different damage rating\nThe first gun you see is called a star blaster and does 2d6 damage.\nThe second gun you see is called a quantum rifle and does 1d12 damage.\nThe third and final gun you see is called a nebula shotgun and does 3d4 damage.")
						gundecision = input(f"Which gun do you choose?\n").lower()
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
			room = floor_2
			save(health, decision, inventory, room)
			floor_2(health, decision, inventory)
def floor_2(health, decision, inventory):
				Final_Boss = ""
				guard2 = 5
				print(f'You step out onto the second floor of the ship and immediantly there are two guards at the doorway who grab you.\nOne of the guards says "where do you think youre going bucko?"\nAs they are carying you down a hall one of them slips on a banna peel somebody must have left on the floor.\nYou break free from the guards grip.')
				decision = input(f'You draw your blaster and look at the guard standing up.\nType "shoot" to shoot at the guard standing up.\n').lower()
				while guard2 >= 0:
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
				print(f'This time the guards wont let you go so easily\nBefore you can do anything a guard comes up behind you and knocks you out.\n\n\n\n')
				room = floor_3
				save(health, decision, inventory, room)
				floor_3(health, inventory, decision)
				decision = ''
def floor_3(health, inventory, decision):
		key = ''
		key_in_inventory = 0
		test = ""
		test_2 = ""
		while health != 0:
			if health <= 0:
				break
			decision = input(f'You wake up in a new cell on a different floor except this time the door is locked.\nType "open" to try and open the door\nType "shoot" to try and shoot the door open\n').lower()
			if decision == "open":
				print(f"You manage to get the door open despite it being locked and enter a long hallway")
			elif decision == "shoot":
				print(f'You blast open the door with a loud "bang" and for a second\nYou think you are fine but then 5 guards come running to your door and unload on you\n')
				Ratta_shooty = random.randint(1,6)
				total = Ratta_shooty * 5
				health = health - total
				if health <= 0:
					death()
					break
					main()
				else:
					print(f"The guards do {total} points of damage of damage getting your health down to {health}\nSomehow they dont kill you and you unload with your gun killing each guard\ncongrats you arent dead YET")
			decision = input(f'When you enter the hall you have 3 options\nGo strait into a room\nGo right into the spaceships bridge\nOr go left into large training area\nType "left" "right" or "strait"\n').lower()
			test_1 = 1
			while decision != 'done':
				if health <= 0:
					break
				if test_1 == 0:
					decision = input(f'You have three options\nGo right into the spaceships bridge\nOr go left into large training area\nType "left" "right" or "strait"\n').lower()
				if decision == "strait":
					print(f"You enter the room strait ahead of you\nIn this room there is a massive screen that apears to be turned off\nThe door slams shut behind you and the screen turns on")
					decision = input(f'The screen turns on with a loud voice to greet you\nIt says "Hello player welcome to space trivia, would you like to play?"\nType "yes" to play or "no" to not play\n').lower()
					if decision == "no":
						print(f'A gun comes out of the wall and shoots you doing 3 points of damage\nThe voice says "sorry not sorry"')
						health = health -3
						if health <= 0:
							death()
							health_fix(health)
							break
							main()
					print(f'The computer says "Im so glad you decided to play"\n"Lets get started"')
					decision = input(f'"There will be 3 trivia questions each time you get one wrong I will punish you"\n"First question: How many moons does earth have?"\n').lower()
					if decision == "1":
						print(f'"Correct!"')
					else:
						print(f'"Wrong!"\nA gun comes out of the wall and shoots you doing 3 points of damage')
						health = health -3
						if health <= 0:
							death()
							health_fix(health)
							break
							main()
					decision = input(f'"Second question: How many planets are there in our solar system?"\n').lower()
					if decision == "8":
						print(f'"Correct!"')
					else:
						print(f'"Wrong!"\nA gun comes out of the wall and shoots you doing 3 points of damage')
						health = health -3
						if health <= 0:
							death()
							health_fix(health)
							break
							main()
					decision = input(f'"Final question: Which planet is closest to the sun"\n').lower()
					if decision == "mercury":
						print(f'"Correct!"')
					else:
						print(f'"Wrong!"\nA gun comes out of the wall and shoots you doing 3 points of damage')
						health = health -3
						if health <= 0:
							death()
							health_fix(health)
							break
							main()
					print(f'"You finished my trivia! I will let you go now"\nA door opens letting you out of the room\nYour health currently is {health} points')
				elif decision == "right" and key_in_inventory == 1:
					test_2 = 1
					break
				elif decision == "right" and key_in_inventory == 0:
					print(f"You must have a key to enter this room")
				elif decision == "left":
					key_in_inventory = 1
					print(f"You enter the training area\nYou see a large empty space with targets all around you and a loud voice starts speeking over the speakers")
					print(f'The speakers announce "there is a prisoner in the training room! Units 501 get in there and take him out"\nFor a second there is peace until 3 soldiers barge into the room blasters drawn')
					decision = input(f'You pull out you blaster as well and can point it at any of the 3 guards\nOne might be the captain of this unit and taking him out might get the rest to leave\nWhich guard do you shoot 1, 2 or 3?\n').lower()
					if decision == "3":
						print(f'You take a shot at the 3rd guard and he falls to the ground\nThe other 2 guards look at each other and run out of the room in a panic\nYou must have shot the captain\nYou check his pockets and find a key that he was holding\nYou may now open the door to the right')
					elif decision == "2" or "3":
						print(f'You take a shot at the guard and he falls to the ground\nThe 3rd guard lookes at you and says "You killed Bob, You will pay for that"\nHe and the other guard open fire on you and does 5 points of damage')
						health = health - 5
						if health <= 0:
							death()
							health_fix(health)
							break
							main()
						print(f'You take a shot at the 3rd guard ths time and he falls to the ground\nThe other guard runs out of the room in a panic\nYou must have shot the captain\nYou check his pockets and find a key that he was holding\nYou may now open the door to the right')
				test_1 = 0
			if test_2 == 1:
				print(f'You enter the spaceships bridge\nThere apears to be only one guy who is sitting in a chair\nHe gets up and looks strait into your eyes\nThis is gonna be a duel to the death and you have to be careful on how you proceed')
				decision = input(f"You both have a hand on your gun\nIn order to shoot the guy you have to win a at least one coin flip out of two\nWhat is your guess?\n").lower()
				if decision == "heads":
					decision = input(f"You get one more attempt\nWhat is your choice?\n").lower()
					if decision == "heads":
						print(f"You both draw your blasters but he getss his out first and shoots you strait in the heart\n")
						health = health - 20
						if health <= 0:
							death()
							health_fix(health)
							break
							main()
					elif decision == "tails":
						print(f"You both draw your blasters and you are able to shoot him before he shoots you")
				elif decision == "tails":
					decision = input(f"You get one more attempt\nWhat is your choice?\n").lower()
					print(f"You both draw your blasters and you are able to shoot him before he shoots you")
				print(f"The captain you just shot sits there on the floor and you can tell he is dead\nYou see a beeping red light on a control pannel and out side the window you see the ship heading strait for a planet.\nYou have to escape the ship now or you die.")
				room = floor_4
				save(health, decision, inventory, room)
				floor_4(health, inventory, decision)
				break
def floor_4(health, inventory, decision):
	Final_Boss = 15
	decision = ""
	print(f'You run out of the room and hall and manage to make your way back onto an elevator\nWhen the door opens to the hanger you see a larger man guarding the last space ship out\nHe looks at you and says "You are the one who caused all of the trouble, this is going to be fun"\nThe man pulls out a lightsaber\n')
	while health != 0:
		decision = input(f'The man jumps towards you with a downwards swing\nYou can either Jump by typing "j"\nDuck by typing "d"\nRoll to the right by typing "r"\nOr roll to the left by typing "l"\n').lower()
		if decision == "l" or decision == "r":
			Final_Boss = Final_Boss - 5
			print(f'You jump out of the way of his swing and have a chance to take a shot at him\nYou blast him in the leg and deal 5 points of damage to him\nHis health is now {Final_Boss}\nHe glances at you and says "Dont try that agian or ill take your head off"')
		elif decision == "j" or decision == "d":
			health = health - 5
			print(f'You try and get out of the way of his saber but end up getting hit in the process\nWith a striking blow he does 5 points of damage to you\nYour health is now {health}\nHe glances at you and says "Move out of the way or you will be hit with my blade"')
			if health <= 0:
				death()
				health_fix(health)
				break
				main()
		print(f"You are quite the tough bugger to have gotten this far\nBut ill make this quick\nThis time he throws a grenade strait underneath you")
		decision = input(f'You can either try to toss the grenade back by typing "t"\nJump out of the way by typing "j"\nOr Dive out of the way by typing "d"\n').lower()
		if decision == "t":
			Final_Boss = Final_Boss - 5
			print(f"You grab the grenade and throw it back right before it blows\nIt lands right below the mans feet and explodes doing 5 point of damage to him\nHis health is now {Final_Boss}\nHe gets up from the blast and gives a loud yell")
		elif decision == "j":
			health = health - 2
			print(f'You jump out of the way and the grenade blows up\nSince you were mostly out of the way the grenade only does 2 points of damage\nYour health is now {health}\nHe stairs at you on the ground and laughs')
			if health <= 0:
				death()
				health_fix(health)
				break
				main()
		elif decision == "d":
			print(f'You dive out of the way and the grenade does not hit you\nYour and his health remain the same\nHe looks at you and says "You got lucky this time"')
		decision = input(f'He looks at you with a menacing stare and says "Im going to put sum dirt in your eye"\nHe runs towards you with his lightsaber and swings to the left\nYou can either Jump by typing "j"\nDuck by typing "d"\nRoll to the right by typing "r"\nOr roll to the left by typing "l"\n').lower()
		if decision == "j" or decision == "d":
			Final_Boss = Final_Boss - 5
			print(f'You get out of the way of his swing and have a chance to take a shot at him\nYou blast him in the leg and deal 5 points of damage to him\nHis health is now {Final_Boss}')
		elif decision == "l" or decision == "r":
			health = health - 5
			print(f'You try and get out of the way of his saber but end up getting hit in the process\nWith a striking blow he does 5 points of damage to you\nYour health is now {health}')
			if health <= 0:
				death()
				health_fix(health)
				break
				main()
		break
	print(f"He stumbles after the swing and falls out of the spaceship through a the hanger window and is gone\nCongrats you beat the final boss!\nThe story comes to a close with you getting on a spaceship and fly back to earth\nNobody else knows about what happened on that ship but you will always remember that adventure")
	health = 0
	main()
def death():
	print(f'your health got below 0')
	print("					YOU DIED")
	print("				Better luck next time!")
def health_fix(health):
	if health < 0:
		health = health + (-health)
def save(health, decision, inventory, room):
	decision = input(f"Would you like to save your game?\n")
	if decision == "yes":
		with open("pickles1.dat", "wb") as file:
			pickle.dump(health, file)
			pickle.dump(decision, file)
			pickle.dump(inventory, file)
			pickle.dump(room, file)