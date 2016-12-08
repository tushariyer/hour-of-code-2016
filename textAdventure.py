#These are imported packages
import random


#Preset Values
#Coordinates of player
player_pos = [0,0]

#Directional input for player coordinates based on the direction entered
nav = {'nx':0,'ny':1,'ex':1,'ey':0,'sx':0,'sy':-1,'wx':-1,'wy':0}

#Rooms are part of an object with their own coordinates. If a player is in a room, the rooms coordinates become the player's coordinates
rooms = {'Entrance Way':[0,0],'Living Room':[1,0],'Dining Room':[1,1],'Kitchen':[0,1],'Hallway':[-1,1],'Bedroom':[-2,1]}
print_pos = [[-2,1],[-1,1],[0,1],[1,1],[0,0],[1,0]]

#Goals is an array of size 2. The first value is if the player has 'collected' the treasure. The second is if the player has 'escaped'
goals_reached = [0,0]

goalxy = list(rooms.values())[random.randrange(0,6)]
while goalxy == [0,0]:
	goalxy = list(rooms.values())[random.randrange(0,6)]



#Processing
def walk():
	user_input = input('Which way do you go?  ')

	if user_input.lower() == 'n' or user_input.lower() == 'e' or user_input.lower() == 's' or user_input.lower() == 'w':
		player_pos[0] += nav['{}x'.format(user_input.lower())]
		player_pos[1] += nav['{}y'.format(user_input.lower())]
		
		try:
			check_pos_validity = list(rooms.keys())[list(rooms.values()).index(player_pos)]
			print('\nYou are in the {}'.format(check_pos_validity))
		except:
			print('\nThat is a wall. You cannot go there.')
			player_pos[0] -= nav['{}x'.format(user_input.lower())]
			player_pos[1] -= nav['{}y'.format(user_input.lower())]
	else:
		print('\nYou cant type that. Use N for north, E for east, S for south, W for west')
	
	#Once the player is in the same room as the treasure
	if player_pos == goalxy and goals_reached[0] == 0:
		goals_reached[0] = 1
		#Let the player know!
		print('You have found the Treasure! Now Leave the house while you still can!')
	
	#If the player has collected the treasure and is back at the starting coordinates	
	if player_pos == [0,0] and goals_reached[0] == 1:
		goals_reached[1] = 1
		#YAY they've won!
		print('Congratulations! You were able to escape before being found!')




#Starting Message
print('You have broken in. Find the treasure and escape! Use N E S W to move around!\n')
ps = [' ',' ',' ',' ',' ',' ']
ps[print_pos.index(player_pos)] = 'x'
print("|---|~~~~|---|---|\n|            |   |\n|---|~~~~|---|---|\n         | x |   |\n         ~~~~~~~~~\n-----------------------------")



#Begin Game
while not goals_reached == [1,1]:
	walk()
	ps = [' ',' ',' ',' ',' ',' ']
	ps[print_pos.index(player_pos)] = 'x'
	print("|---|,,,,|---|---|\n| {}    {}   {} | {} |\n|---|''''|---|---|\n         | {} | {} |\n         '''''''''\n-----------------------------".format(ps[0],ps[1],ps[2],ps[3],ps[4],ps[5]))

#Tushar Iyer