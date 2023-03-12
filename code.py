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



start_node = (550,30)
goal_node = (6,6)
Node_i = 0
Parent_Node_i = -1
initial_c2c = 0
node_state=[initial_c2c, Node_i, Parent_Node_i, start_node]
index=None
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
Parent_Node_i+=1
gni=None
while (Open_list.empty()==False):
	
	nodegen = Open_list.get()
	nodecoord = nodegen[-1]
	nodec2c = nodegen[0]
	Closed_list[nodegen[1]]=[nodec2c,nodegen[2],nodecoord]
	# print("My current parent in open list", nodegen)
	# print("The whole Open list",Open_list)
	if(nodecoord==goal_node):
		print("Woohoo we reached the goal")
		gni=nodegen[1]
		gnc=nodecoord
		break
	Parent_Node_i=nodegen[1]
	new_node_up, new_node_cost_up = gen_up(nodecoord, nodec2c)
	if (screen.get_at(new_node_up)!=(255, 0, 0, 255)):
		if not(any(val[-1] == new_node_up for val in Closed_list.values())):
			if new_node_up not in [tup[3] for tup in Open_list.queue]:
				Node_i+=1
				temp_state = [new_node_cost_up, Node_i, Parent_Node_i, new_node_up]
				# print("Node up generated node",temp_state)
				Open_list.put(temp_state)
			else:
				index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list.queue) if (x, y) == new_node_up)
				if (round(new_node_cost_up,1)<round(Open_list.queue[index][0],1)):
					# print("New Cost rounded",new_node_cost_up)
					Open_list.queue[index][0]=new_node_cost_up
					Open_list.queue[index][2]=nodegen[2]
					# print("*****I went inside and modified during up",Open_list.queue[index])
	# print(Open_list)
	new_node_down, new_node_cost_down = gen_down(nodecoord, nodec2c)
	if (screen.get_at(new_node_down)!=(255, 0, 0, 255)):
		if not(any(val[-1] == new_node_down for val in Closed_list.values())):
			if new_node_down not in [tup[3] for tup in Open_list.queue]:
				Node_i+=1
				temp_state = [new_node_cost_down, Node_i, Parent_Node_i, new_node_down]
				# print("Node down generated node",temp_state)
				Open_list.put(temp_state)
			else:
				index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list.queue) if (x, y) == new_node_down)
				if (round(new_node_cost_down,1)<round(Open_list.queue[index][0],1)):
					Open_list.queue[index][0]=new_node_cost_down
					Open_list.queue[index][2]=nodegen[2]
					# print("*****I went inside and modified during down",Open_list.queue[index])

	new_node_left, new_node_cost_left = gen_left(nodecoord, nodec2c)
	if (screen.get_at(new_node_left)!=(255, 0, 0, 255)):
		if not(any(val[-1] == new_node_left for val in Closed_list.values())):
			if new_node_left not in [tup[3] for tup in Open_list.queue]:
				Node_i+=1
				temp_state = [new_node_cost_left, Node_i, Parent_Node_i, new_node_left]
				# print("Node left generated node",temp_state)
				Open_list.put(temp_state)
			else:
				index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list.queue) if (x, y) == new_node_left)
				if (round(new_node_cost_left,1)<round(Open_list.queue[index][0],1)):
					Open_list.queue[index][0]=new_node_cost_left
					Open_list.queue[index][2]=nodegen[2]
					# print("*****I went inside and modified during left",Open_list.queue[index])

	new_node_right, new_node_cost_right = gen_right(nodecoord, nodec2c)
	if (screen.get_at(new_node_right)!=(255, 0, 0, 255)):
		if not(any(val[-1] == new_node_right for val in Closed_list.values())):
			if new_node_right not in [tup[3] for tup in Open_list.queue]:
				Node_i+=1
				temp_state = [new_node_cost_right, Node_i, Parent_Node_i, new_node_right]
				# print("Node right generated node",temp_state)
				Open_list.put(temp_state)
			else:
				index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list.queue) if (x, y) == new_node_right)
				if (round(new_node_cost_right,1)<round(Open_list.queue[index][0],1)):
					Open_list.queue[index][0]=new_node_cost_right
					Open_list.queue[index][2]=nodegen[2]
					# print("*****I went inside and modified during right",Open_list.queue[index])

	new_node_up_left, new_node_cost_up_left = gen_up_left(nodecoord, nodec2c)
	if (screen.get_at(new_node_up_left)!=(255, 0, 0, 255)):
		if not(any(val[-1] == new_node_up_left for val in Closed_list.values())):
			if new_node_up_left not in [tup[3] for tup in Open_list.queue]:
				Node_i+=1
				temp_state = [new_node_cost_up_left, Node_i, Parent_Node_i, new_node_up_left]
				# print("Node up left generated node",temp_state)
				Open_list.put(temp_state)
			else:
				index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list.queue) if (x, y) == new_node_up_left)
				if (round(new_node_cost_up_left,1)<round(Open_list.queue[index][0],1)):
					Open_list.queue[index][0]=new_node_cost_up_left
					Open_list.queue[index][2]=nodegen[2]
					# print("*****I went inside and modified during up left",Open_list.queue[index])

	new_node_up_right, new_node_cost_up_right = gen_up_right(nodecoord, nodec2c)
	if (screen.get_at(new_node_up_right)!=(255, 0, 0, 255)):
		if not(any(val[-1] == new_node_up_right for val in Closed_list.values())):
			if new_node_up_right not in [tup[3] for tup in Open_list.queue]:
				Node_i+=1
				temp_state = [new_node_cost_up_right, Node_i, Parent_Node_i, new_node_up_right]
				print("Node up right generated node",temp_state)
				Open_list.put(temp_state)
			else:
				index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list.queue) if (x, y) == new_node_up_right)
				if (round(new_node_cost_up_right,1)<round(Open_list.queue[index][0],1)):
					Open_list.queue[index][0]=new_node_cost_up_right
					Open_list.queue[index][2]=nodegen[2]
					print("*****I went inside and modified during up right", Open_list.queue[index])

	new_node_down_left, new_node_cost_down_left = gen_down_left(nodecoord, nodec2c)
	if (screen.get_at(new_node_down_left)!=(255, 0, 0, 255)):
		if not(any(val[-1] != new_node_down_left for val in Closed_list.values())):
			if new_node_down_left not in [tup[3] for tup in Open_list.queue]:
				Node_i+=1
				temp_state = [new_node_cost_down_left, Node_i, Parent_Node_i, new_node_down_left]
				print("Node down left generated node",temp_state)
				Open_list.put(temp_state)
			else:
				index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list.queue) if (x, y) == new_node_down_left)
				if (round(new_node_cost_down_left,1)<round(Open_list.queue[index][0],1)):
					Open_list.queue[index][0]=new_node_cost_down_left
					Open_list.queue[index][2]=nodegen[2]
					print("*****I went inside and modified during down left", Open_list.queue[index])

	new_node_down_right, new_node_cost_down_right = gen_down_right(nodecoord, nodec2c)
	if (screen.get_at(new_node_down_right)!=(255, 0, 0, 255)):
		if not(any(val[-1] == new_node_down_right for val in Closed_list.values())):
			if new_node_down_right not in [tup[3] for tup in Open_list.queue]:
				Node_i+=1
				temp_state = [new_node_cost_down_right, Node_i, Parent_Node_i, new_node_down_right]
				print("Node down right generated node",temp_state)
				Open_list.put(temp_state)
			else:
				index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list.queue) if (x, y) == new_node_down_right)
				if (round(new_node_cost_down_right,1)<round(Open_list.queue[index][0],1)):
					Open_list.queue[index][0]=new_node_cost_down_right
					Open_list.queue[index][2]=nodegen[2]
					print("******I went inside and modified during down right",Open_list.queue[index])
	screen.set_at(nodecoord,(255,0,255))
	pyg.display.update()
	
print(Closed_list)	
path=[]
# path.append(gnc)
while gni!=-1:
	path.append(Closed_list[gni][-1])
	gni=Closed_list[gni][1]
	print(1)
path.reverse()
print(path)
# for valu in Closed_list.values():
# 	screen.set_at(valu[-1],(255,0,255))
# 	pyg.display.update()	
for co in path:
	screen.set_at(co,(0,0,0))
	pyg.display.update()


while running:
	# for loop through the event queue
	for event in pyg.event.get():
		# Check for QUIT event	
		if event.type == pyg.QUIT:
			running = False
