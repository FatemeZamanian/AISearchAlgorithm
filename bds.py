import copy
from treelib import Tree
from utils import *
from node import Node
from colorama import Fore


nodes = []


def get_path(node):
    path = []
    this_node = node
    while this_node.parent != None:
        this_node = this_node.parent
        path.append(copy.deepcopy(this_node))
    return path





def check():
    for n1 in nodes:
        for n2 in nodes:
            if n1.dir == 'r' and n2.dir == 'l' and n1.pos == n2.pos:
                print("A path Found, checking for scores condition...")
                left_path=get_path(n2)
                this_node=n1
                for node in left_path:
                    set_op(this_node,node)
                    this_node=node
                

                if this_node.agent_score > this_node.goal_score:
                    print(Fore.GREEN, "Scores condition is OK :)", Fore.RESET)
                    print("agent score:", this_node.agent_score)
                    print("goal score:", this_node.goal_score)
                    print_path_bi_directional(n1, n2)
                    exit()
                else:
                    print(Fore.RED, "Scores condition is not OK :(", Fore.RESET)


def bds(mat):
    start_pos = find_root(mat)
    goal_pos = find_goal(mat)
    goal = Node(goal_pos, mat,dir='l')
    start = Node(start_pos, mat,dir='r') # No parent means its the root node

    start.agent_score = start.get_number()
    start.goal_score = goal.get_number()

    nodes.append(start)
    nodes.append(goal)
    q = []
    q.append(start)
    q.append(goal)
    while len(q) > 0:
        this_node = q.pop(0)

        check()
        
        neighbors = find_neighbors(mat,this_node,this_node.dir)
        for neighbor in neighbors:
            if neighbor.pos not in this_node.visited_nodes:
                q.append(neighbor)
                nodes.append(neighbor)
            
    print("Not found")
    print("agent score:", this_node.agent_score)
    print("goal score:", this_node.goal_score)
    
