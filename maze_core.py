


def room1():
	print "You awaken in a small room, the door behind you is locked shut \nThe is a door ahead of you. Type N to go north."

	choice = raw_input("> ")

	if choice == "N":
		print "You head through the door to the next room."
		room2()

	else:
		print "That doesn't make any sense..."
		room1()


def room2():
	print "This room has a door to the North and a door to the east"

	choice = raw_input("> ")

	if choice == "N":
		print "You head North"
		room4()
	elif choice == "E":
		print "You head east"
		room3()
	else:
		print "Wait, what?"
		room2()


def room3():
	print "As you pass through the door a trap opens above you and a large rock land on your head"
	dead()


def room4():
	print "You enter a green room. This room has a door to the North and a door to the West"

	choice = raw_input("> ")

	if choice == "N":
		print "You head North"
		room9()
	elif choice == "W":
		print "You head West"
		room5()
	else:
		print "Wait, what?"
		room4()

def room5():
	print "You enter a room with 5 stones in the center and a door to the West"

	choice = raw_input("> ")

	if choice == "W":
		print "You head West"
		room6()
	else:
		print "Wait, what?"
		room5()


def room6():
	print "You enter a room with a pool of water and a door to the south."

	choice = raw_input("> ")

	if choice == "S":
		print "You head South"
		room7()
	else:
		print "Wait, what?"
		room6()

def room7():
	print "You enter the room and are charged by a monster. Quick, head through the door to the West!"

	choice = raw_input("> ")

	if choice == "W":
		print "You quickly dive through the door to the West and escape. Phew, that was close!"
		room8()
	else:
		print "You hesitate and the monster bites your head off!"
		dead()	

def room8():
	print "You made it! You have escaped the Maze of death! Do you want to play again?"

	choice = raw_input("> ")

	if choice == "Y":
		room1()

	elif choice == "N":
		print "Bye Bye then..."
		exit(0)

	else:
		print "Wait, what?"
		room8()


def room9():
	print "A pit opens under you and you fall to your death!"
	dead()



def dead():
	print "You are dead, do you want to try again? Y or N"

	choice = raw_input("> ")

	if choice == "Y":
		room1()

	elif choice == "N":
		print "Bye Bye then..."
		exit(0)

	else:
		print "Wait, what?"
		dead()

room1()
