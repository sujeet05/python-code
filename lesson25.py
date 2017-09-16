from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"
	next = raw_input(">")
	if "0" in next or "1" in next:
		how_much= int(next)
	else:
		dead("man,Learn to type a number")
	if how_much <50:
		print " you are not greedy,you win !"
		exit(0)
	else:
		dead("you greedy bastard!")

def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
 	print "How are you going to move the bear?"
 	bear_moved= False
 	while True:
 		next=raw_input(">")
 		if(next=="takehoney"):
 			dead("The bear looks at you then slaps your face off.")
 		elif(next=="taunt bear" and not bear_moved):
 			print "The bear has moved from the door. You can go through it now."
 			bear_moved = True
 		elif(next=="taunt bear" and bear_moved):
 			dead("The bear gets pissed off and chews your leg off.")
 		elif(next=="open door" and bear_moved):
			gold_room()			
 		else :
 			print " i got no idea what that means "

def ethulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"

	next=raw_input(">")
	if("flee" in next):
		start()
	elif("head" in next):
		dead("well that was testy")
	else:
		cthulhu_room()
#helper function
def dead(why):
	print why ,"Good Job!!!"
	exit(0)
def start():
	print "you are in dark room "
	print "There is a door to your left and right"
	print "Enter left or right "
	next= raw_input("Left or Right ?")
	if(next=="Left"):
		bear_room();
	elif(next=="Right"):
		ethulhu_room()
	else:
		dead("You stumble around the room until you starve.")
start();