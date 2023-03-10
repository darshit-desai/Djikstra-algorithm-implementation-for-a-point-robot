# import the pygame module
import pygame as pyg
import numpy as np
from queue import PriorityQueue

# Define the background colour
# using RGB color coding.

# Define the dimensions of
# screen object(width,height)
screen = pyg.display.set_mode((600, 250))
rect_color = (255, 255, 255)
rectangle1 = pyg.Rect(5, 5, 590, 240)
screen.fill((255,0,0))
pyg.draw.rect(screen, rect_color, rectangle1)
pyg.draw.rect(screen, (255,0,0),pyg.Rect(95,145,60,105))
pyg.draw.rect(screen, (255,0,0),pyg.Rect(95,0,60,105))
hexagon_dim = [(300,44.22649731),(230.04809472,84.61324865),(230.04809472,165.38675135),(300,205.77350269),(369.95190528,165.38675135),(369.95190528,84.61324865)]
pyg.draw.polygon(screen,(255,0,0),hexagon_dim)
triangle_dim = [(455,246.18033989),(455.00,3.81966011),(515.59016994,125)]
pyg.draw.polygon(screen,(255,0,0),triangle_dim)
# Set the caption of the screen
pyg.display.set_caption('Djikstra')

# Fill the background colour to the screen


# Update the display using flip
pyg.display.update()

# Variable to keep our game loop running
running = True

# game loop



start_node = (5,5)
goal_node = (400,125)
Node_i = 0
Parent_Node_i = -1
initial_c2c = 0
node_state=[initial_c2c, Node_i, Parent_Node_i, start_node]

Open_list = PriorityQueue()
Open_list.put(node_state)
Closed_list = {}

def gen_up(node,nc2c):
	nnode = (node[0]+0,node[1]-1)
	cost = nc2c+1
	return nnode, cost
def gen_down(node,nc2c):
	nnode = (node[0]+0,node[1]+1)
	cost = nc2c+1
	return nnode, cost
def gen_left(node,nc2c):
	nnode = (node[0]-1,node[1]+0)
	cost = nc2c+1
	return nnode, cost
def gen_right(node,nc2c):
	nnode = (node[0]+1,node[1]+0)
	cost = nc2c+1
	return nnode, cost
def gen_up_left(node, nc2c):
	nnode = (node[0]-1,node[1]-1)
	cost = nc2c + 1.4
	return nnode, cost
def gen_up_right(node, nc2c):
	nnode = (node[0]+1,node[1]-1)
	cost = nc2c + 1.4
	return nnode, cost
def gen_down_left(node, nc2c):
	nnode = (node[0]-1,node[1]+1)
	cost = nc2c + 1.4
	return nnode, cost
def gen_down_right(node, nc2c):
	nnode = (node[0]+1,node[1]+1)
	cost = nc2c + 1.4
	return nnode, cost

while (Open_list.empty()==False):
	
	nodegen = Open_list.get()
	nodecoord = nodegen[-1]
	nodec2c = nodegen[0]
	Closed_list[Node_i]=[nodec2c,nodegen[2],nodecoord]
	print(Closed_list)
	if(nodecoord==goal_node):
		break
	Parent_Node_i+=1
	new_node_up, new_node_cost_up = gen_up(nodecoord, nodec2c)
	
	if (screen.get_at(new_node_up)!=(255, 0, 0, 255)):
		if not(any(map(lambda x:x[2]==new_node_up, Closed_list.items()))):
			if new_node_up not in [tup[3] for tup in Open_list]:
				Node_i+=1
				temp_state = [new_node_cost_up, Node_i, Parent_Node_i, new_node_up]
				Open_list.put(temp_state)
			else:
				index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list) if (x, y) == new_node_up)
				if (new_node_cost_up<Open_list[index][0]):
					Open_list[index][0]=new_node_cost_up
					Open_list[index][2]=nodegen[2]
	
	new_node_down, new_node_cost_down = gen_down(nodecoord, nodec2c)
	if (screen.get_at(new_node_down)!=(255, 0, 0, 255)):
		if not(any(map(lambda x:x[2]==new_node_down, Closed_list.items()))):
			if new_node_down not in [tup[3] for tup in Open_list]:
				Node_i+=1
				temp_state = [new_node_cost_down, Node_i, Parent_Node_i, new_node_down]
				Open_list.put(temp_state)
			else:
				index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list) if (x, y) == new_node_down)
				if (new_node_cost_down<Open_list[index][0]):
					Open_list[index][0]=new_node_cost_down
					Open_list[index][2]=nodegen[2]

	new_node_left, new_node_cost_left = gen_left(nodecoord, nodec2c)
	if (screen.get_at(new_node_left)!=(255, 0, 0, 255)):
		if not(any(map(lambda x:x[2]==new_node_left, Closed_list.items()))):
			if new_node_left not in [tup[3] for tup in Open_list]:
				Node_i+=1
				temp_state = [new_node_cost_left, Node_i, Parent_Node_i, new_node_left]
				Open_list.put(temp_state)
			else:
				index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list) if (x, y) == new_node_left)
				if (new_node_cost_left<Open_list[index][0]):
					Open_list[index][0]=new_node_cost_left
					Open_list[index][2]=nodegen[2]

	new_node_right, new_node_cost_right = gen_right(nodecoord, nodec2c)
	if (screen.get_at(new_node_right)!=(255, 0, 0, 255)):
		if not(any(map(lambda x:x[2]==new_node_right, Closed_list.items()))):
				if new_node_right not in [tup[3] for tup in Open_list]:
					Node_i+=1
					temp_state = [new_node_cost_right, Node_i, Parent_Node_i, new_node_right]
					Open_list.put(temp_state)
				else:
					index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list) if (x, y) == new_node_right)
					if (new_node_cost_right<Open_list[index][0]):
						Open_list[index][0]=new_node_cost_right
						Open_list[index][2]=nodegen[2]

	new_node_up_left, new_node_cost_up_left = gen_up_left(nodecoord, nodec2c)
	if (screen.get_at(new_node_up_left)!=(255, 0, 0, 255)):
		if not(any(map(lambda x:x[2]==new_node_up_left, Closed_list.items()))):
				if new_node_up_left not in [tup[3] for tup in Open_list]:
					Node_i+=1
					temp_state = (new_node_cost_up_left, Node_i, Parent_Node_i, new_node_up_left)
					Open_list.put(temp_state)
				else:
					index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list) if (x, y) == new_node_up_left)
					if (new_node_cost_up_left<Open_list[index][0]):
						Open_list[index][0]=new_node_cost_up_left
						Open_list[index][2]=nodegen[2]

	new_node_up_right, new_node_cost_up_right = gen_up_right(nodecoord, nodec2c)
	if (screen.get_at(new_node_up_right)!=(255, 0, 0, 255)):
		if not(any(map(lambda x:x[2]==new_node_up_right, Closed_list.items()))):
				if new_node_up_right not in [tup[3] for tup in Open_list]:
					Node_i+=1
					temp_state = [new_node_cost_up_right, Node_i, Parent_Node_i, new_node_up_right]
					Open_list.put(temp_state)
				else:
					index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list) if (x, y) == new_node_up_right)
					if (new_node_cost_up_right<Open_list[index][0]):
						Open_list[index][0]=new_node_cost_up_right
						Open_list[index][2]=nodegen[2]

	new_node_down_left, new_node_cost_down_left = gen_down_left(nodecoord, nodec2c)
	if (screen.get_at(new_node_down_left)!=(255, 0, 0, 255)):
		if not(any(map(lambda x:x[2]==new_node_down_left, Closed_list.items()))):
				if new_node_down_left not in [tup[3] for tup in Open_list]:
					Node_i+=1
					temp_state = [new_node_cost_down_left, Node_i, Parent_Node_i, new_node_down_left]
					Open_list.put(temp_state)
				else:
					index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list) if (x, y) == new_node_down_left)
					if (new_node_cost_down_left<Open_list[index][0]):
						Open_list[index][0]=new_node_cost_down_left
						Open_list[index][2]=nodegen[2]

	new_node_down_right, new_node_cost_down_right = gen_down_right(nodecoord, nodec2c)
	if (screen.get_at(new_node_down_right)!=(255, 0, 0, 255)):
		if not(any(map(lambda x:x[2]==new_node_down_right, Closed_list.items()))):
				if new_node_down_right not in [tup[3] for tup in Open_list]:
					Node_i+=1
					temp_state = [new_node_cost_down_right, Node_i, Parent_Node_i, new_node_down_right]
					Open_list.put(temp_state)
				else:
					index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list) if (x, y) == new_node_down_right)
					if (new_node_cost_down_right<Open_list[index][0]):
						Open_list[index][0]=new_node_cost_down_right
						Open_list[index][2]=nodegen[2]
	

while running:
	# for loop through the event queue
	for event in pyg.event.get():
		# Check for QUIT event	
		if event.type == pyg.QUIT:
			running = False
