# import the pygame module
import pygame as pyg
import numpy as np
#import queue module
from queue import PriorityQueue
import time

#Note: All obstacle dimensions are inflated to cover the point robot radius of 5 mm or 5 pixels. You will see the 
#same in the visualisation

#Define the Surface Map
screen = pyg.Surface((600, 250))
#Define the rectangles which make the base map
rect_color = (255, 255, 255)
#Define the rectangle which makes the outer border
rectangle1 = pyg.Rect(5, 5, 590, 240)
screen.fill((255,0,0))
pyg.draw.rect(screen, rect_color, rectangle1)
#Define the rectangle which makes the 2 rectangles
pyg.draw.rect(screen, (255,0,0),pyg.Rect(95,145,60,105))
pyg.draw.rect(screen, (255,0,0),pyg.Rect(95,0,60,105))
#Define the hexagon in the center
hexagon_dim = [(300,44.22649731),(230.04809472,84.61324865),(230.04809472,165.38675135),(300,205.77350269),(369.95190528,165.38675135),(369.95190528,84.61324865)]
pyg.draw.polygon(screen,(255,0,0),hexagon_dim)
triangle_dim = [(455,246.18033989),(455.00,3.81966011),(515.59016994,125)]
pyg.draw.polygon(screen,(255,0,0),triangle_dim)
# Set the caption of the screen
pyg.display.set_caption('Djikstra')

# Variable to keep our game loop running
running = True

#Condition which asks the user for their inputs
while True:
	start_x = int(input("Please enter the x coordinate of start:"))
	start_y = int(input("Please enter the y coordinate of start:"))
	goal_x = int(input("Please enter the x coordinate of goal:"))
	goal_y = int(input("Please enter the y coordinate of goal:"))
	start_y = 250-(start_y)
	goal_y = 250-(goal_y)
	if (screen.get_at((goal_x,goal_y))!=(255,0,0,255) and screen.get_at((start_x,start_y))!=(255,0,0,255)): 
		print("Valid coordinates received")
		break
	else:
		print("Invalid coordinates try again")

#Djikstra Starts here
#Start time to measure time of run of algorithm
start_time = time.time()

#Definitions of initial conditions of Djikstra like start node goal node indices
start_node = (start_x,start_y)
goal_node = (goal_x,goal_y)
Node_i = 0
Parent_Node_i = -1
initial_c2c = 0
node_state=[initial_c2c, Node_i, Parent_Node_i, start_node]
index=None
Open_list = PriorityQueue()
Open_list.put(node_state)
Closed_list = {}
goalreached = 0


#Action set function which updates coordinates and actions
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

#Parent Node incremented to be ready for the next node
Parent_Node_i+=1
#Variable used for tracking goal node index
gni=None
#Main iterator starts
while (Open_list.empty()==False):
	#Pop the first node of open list
	nodegen = Open_list.get()
	nodecoord = nodegen[-1]
	nodec2c = nodegen[0]
	Closed_list[nodegen[1]]=[nodec2c,nodegen[2],nodecoord]
	print("Latest generated node:",nodegen)
	#Check whether we found the goal node or not
	if(nodecoord==goal_node):
		print("Woohoo we reached the goal")
		goalreached=1
		gni=nodegen[1]
		gnc=nodecoord
		break
	#Assign the latest popped node index as parent node
	Parent_Node_i=nodegen[1]
	
	#Code which generates and checks the up action coordinates for validity to update in open list or modify the cost
	new_node_up, new_node_cost_up = gen_up(nodecoord, nodec2c)
	if (new_node_up==goal_node):
		Node_i+=1
		gni = Node_i
		Closed_list[Node_i]=[new_node_cost_up,Parent_Node_i,new_node_up]
		print("Goal Reached after doing up operation")
		goalreached=1
		break
	if (screen.get_at(new_node_up)!=(255, 0, 0, 255)):
		if not(any(val[-1] == new_node_up for val in Closed_list.values())): #Check if in closed list
			if new_node_up not in [tup[3] for tup in Open_list.queue]:	#Check if in open list
				Node_i+=1
				temp_state = [new_node_cost_up, Node_i, Parent_Node_i, new_node_up]
				Open_list.put(temp_state)
			else:
				index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list.queue) if (x, y) == new_node_up)
				if (round(new_node_cost_up,1)<round(Open_list.queue[index][0],1)): #if in open list update cost
					Open_list.queue[index][0]=new_node_cost_up
					Open_list.queue[index][2]=nodegen[2]
	
	#Code which generates and checks the down action coordinates for validity to update in open list or modify the cost
	new_node_down, new_node_cost_down = gen_down(nodecoord, nodec2c)
	if (new_node_down==goal_node):
		Node_i+=1
		gni = Node_i
		Closed_list[Node_i]=[new_node_cost_down,Parent_Node_i,new_node_down]
		print("Goal Reached after doing down operation")
		goalreached=1
		break
	if (screen.get_at(new_node_down)!=(255, 0, 0, 255)):
		if not(any(val[-1] == new_node_down for val in Closed_list.values())):
			if new_node_down not in [tup[3] for tup in Open_list.queue]:
				Node_i+=1
				temp_state = [new_node_cost_down, Node_i, Parent_Node_i, new_node_down]
				Open_list.put(temp_state)
			else:
				index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list.queue) if (x, y) == new_node_down)
				if (round(new_node_cost_down,1)<round(Open_list.queue[index][0],1)):
					Open_list.queue[index][0]=new_node_cost_down
					Open_list.queue[index][2]=nodegen[2]

	#Code which generates and checks the left action coordinates for validity to update in open list or modify the cost
	new_node_left, new_node_cost_left = gen_left(nodecoord, nodec2c)
	if (new_node_left==goal_node):
		Node_i+=1
		gni = Node_i
		Closed_list[Node_i]=[new_node_cost_left,Parent_Node_i,new_node_left]
		print("Goal Reached after doing left operation")
		goalreached=1
		break
	if (screen.get_at(new_node_left)!=(255, 0, 0, 255)):
		if not(any(val[-1] == new_node_left for val in Closed_list.values())):
			if new_node_left not in [tup[3] for tup in Open_list.queue]:
				Node_i+=1
				temp_state = [new_node_cost_left, Node_i, Parent_Node_i, new_node_left]
				Open_list.put(temp_state)
			else:
				index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list.queue) if (x, y) == new_node_left)
				if (round(new_node_cost_left,1)<round(Open_list.queue[index][0],1)):
					Open_list.queue[index][0]=new_node_cost_left
					Open_list.queue[index][2]=nodegen[2]

	#Code which generates and checks the right action coordinates for validity to update in open list or modify the cost
	new_node_right, new_node_cost_right = gen_right(nodecoord, nodec2c)
	if (new_node_right==goal_node):
		Node_i+=1
		gni = Node_i
		Closed_list[Node_i]=[new_node_cost_right,Parent_Node_i,new_node_right]
		print("Goal Reached after doing right operation")
		goalreached=1
		break
	if (screen.get_at(new_node_right)!=(255, 0, 0, 255)):
		if not(any(val[-1] == new_node_right for val in Closed_list.values())):
			if new_node_right not in [tup[3] for tup in Open_list.queue]:
				Node_i+=1
				temp_state = [new_node_cost_right, Node_i, Parent_Node_i, new_node_right]
				Open_list.put(temp_state)
			else:
				index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list.queue) if (x, y) == new_node_right)
				if (round(new_node_cost_right,1)<round(Open_list.queue[index][0],1)):
					Open_list.queue[index][0]=new_node_cost_right
					Open_list.queue[index][2]=nodegen[2]

	#Code which generates and checks the up left action coordinates for validity to update in open list or modify the cost
	new_node_up_left, new_node_cost_up_left = gen_up_left(nodecoord, nodec2c)
	if (new_node_up_left==goal_node):
		Node_i+=1
		gni = Node_i
		Closed_list[Node_i]=[new_node_cost_up_left,Parent_Node_i,new_node_up_left]
		print("Goal Reached after doing up left operation")
		goalreached=1
		break
	if (screen.get_at(new_node_up_left)!=(255, 0, 0, 255)):
		if not(any(val[-1] == new_node_up_left for val in Closed_list.values())):
			if new_node_up_left not in [tup[3] for tup in Open_list.queue]:
				Node_i+=1
				temp_state = [new_node_cost_up_left, Node_i, Parent_Node_i, new_node_up_left]
				Open_list.put(temp_state)
			else:
				index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list.queue) if (x, y) == new_node_up_left)
				if (round(new_node_cost_up_left,1)<round(Open_list.queue[index][0],1)):
					Open_list.queue[index][0]=new_node_cost_up_left
					Open_list.queue[index][2]=nodegen[2]

	#Code which generates and checks the up right action coordinates for validity to update in open list or modify the cost
	new_node_up_right, new_node_cost_up_right = gen_up_right(nodecoord, nodec2c)
	if (new_node_up_right==goal_node):
		Node_i+=1
		gni = Node_i
		Closed_list[Node_i]=[new_node_cost_up_right,Parent_Node_i,new_node_up_right]
		print("Goal Reached after doing up right operation")
		goalreached=1
		break
	if (screen.get_at(new_node_up_right)!=(255, 0, 0, 255)):
		if not(any(val[-1] == new_node_up_right for val in Closed_list.values())):
			if new_node_up_right not in [tup[3] for tup in Open_list.queue]:
				Node_i+=1
				temp_state = [new_node_cost_up_right, Node_i, Parent_Node_i, new_node_up_right]
				Open_list.put(temp_state)
			else:
				index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list.queue) if (x, y) == new_node_up_right)
				if (round(new_node_cost_up_right,1)<round(Open_list.queue[index][0],1)):
					Open_list.queue[index][0]=new_node_cost_up_right
					Open_list.queue[index][2]=nodegen[2]

	#Code which generates and checks the down left action coordinates for validity to update in open list or modify the cost
	new_node_down_left, new_node_cost_down_left = gen_down_left(nodecoord, nodec2c)
	if (new_node_down_left==goal_node):
		Node_i+=1
		gni = Node_i
		Closed_list[Node_i]=[new_node_cost_down_left,Parent_Node_i,new_node_down_left]
		print("Goal Reached after doing down left operation")
		goalreached=1
		break
	if (screen.get_at(new_node_down_left)!=(255, 0, 0, 255)):
		if not(any(val[-1] != new_node_down_left for val in Closed_list.values())):
			if new_node_down_left not in [tup[3] for tup in Open_list.queue]:
				Node_i+=1
				temp_state = [new_node_cost_down_left, Node_i, Parent_Node_i, new_node_down_left]
				Open_list.put(temp_state)
			else:
				index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list.queue) if (x, y) == new_node_down_left)
				if (round(new_node_cost_down_left,1)<round(Open_list.queue[index][0],1)):
					Open_list.queue[index][0]=new_node_cost_down_left
					Open_list.queue[index][2]=nodegen[2]

	#Code which generates and checks the down right action coordinates for validity to update in open list or modify the cost
	new_node_down_right, new_node_cost_down_right = gen_down_right(nodecoord, nodec2c)
	if (new_node_down_right==goal_node):
		Node_i+=1
		gni = Node_i
		Closed_list[Node_i]=[new_node_cost_down_right,Parent_Node_i,new_node_down_right]
		print("Goal Reached after doing down right operation")
		goalreached=1
		break
	if (screen.get_at(new_node_down_right)!=(255, 0, 0, 255)):
		if not(any(val[-1] == new_node_down_right for val in Closed_list.values())):
			if new_node_down_right not in [tup[3] for tup in Open_list.queue]:
				Node_i+=1
				temp_state = [new_node_cost_down_right, Node_i, Parent_Node_i, new_node_down_right]
				Open_list.put(temp_state)
			else:
				index = next(i for i, (_, _, _, (x, y)) in enumerate(Open_list.queue) if (x, y) == new_node_down_right)
				if (round(new_node_cost_down_right,1)<round(Open_list.queue[index][0],1)):
					Open_list.queue[index][0]=new_node_cost_down_right
					Open_list.queue[index][2]=nodegen[2]
	
	

#Path Backtracking
path=[]

if (goalreached!=0):
	while gni!=-1:
		path.append(Closed_list[gni][-1])
		gni=Closed_list[gni][1]
else:
	print("Goal not reached")
path.reverse()
print(path)
end_time = time.time()	#Algorithm end time
total_time = end_time - start_time
print(f"Total runtime: {total_time:.2f} seconds") #Final runtime


#Overlay the final canvas and display the pygame simulation
s1 = pyg.display.set_mode((600, 250))
# Blit the surface onto the Pygame window
s1.blit(screen, (0, 0))
# Update the display
pyg.display.update()

for valu in Closed_list.values():
	s1.set_at(valu[-1],(255,0,255))
	pyg.display.update()	
for co in path:
	s1.set_at(co,(0,0,0))
	pyg.time.wait(50)
	pyg.display.update()
pyg.time.wait(1000)
while running:
	# for loop through the event queue
	for event in pyg.event.get():
		# Check for QUIT event	
		if event.type == pyg.QUIT:
			running = False
