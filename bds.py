from treelib import Tree
from utils import *
from node import Node
from colorama import Fore


nodes = []

def check():
    for n1 in nodes:
        for n2 in nodes:
            if n1.dir == 'r' and n2.dir == 'l' and n1.pos == n2.pos:
                print("A path Found, checking for scores condition...")

                try:
                    total_agent_score = n1.agent_score + n2.parent.agent_score
                except:
                    total_agent_score = n1.parent.agent_score + n2.agent_score

                try:
                    total_goal_score = n1.goal_score + n2.parent.goal_score
                except:
                    total_goal_score = n1.parent.goal_score + n2.goal_score

                if total_agent_score > total_goal_score:
                    print(Fore.GREEN, "Scores condition is OK :)", Fore.RESET)
                    print("agent score:", total_agent_score)
                    print("goal score:", total_goal_score)
                    print_path_bi_directional(n1, n2)
                    exit()
                else:
                    print(Fore.RED, "Scores condition is not OK :(", Fore.RESET)


def bds(mat):
    start_pos = find_root(mat)
    goal_pos = find_goal(mat)
    goal = Node(goal_pos, mat,dir='l')
    start = Node(start_pos, mat,dir='r') # No parent means its the root node
    visited=[]

    start.agent_score = start.get_number()
    start.goal_score = goal.get_number()

    goal.agent_score = start.get_number()
    goal.goal_score = goal.get_number()

    nodes.append(start)
    nodes.append(goal)
    q = []
    q.append(start)
    q.append(goal)
    while len(q) > 0:
        this_node = q.pop(0)

        check()
        
        visited.append(this_node.pos)
        neighbors = find_neighbors(mat,this_node,this_node.dir)
        for neighbor in neighbors:
            if neighbor.pos not in this_node.visited_nodes:
                q.append(neighbor)
                nodes.append(neighbor)
            
    print("Not found")
    print("agent score:", this_node.agent_score)
    print("goal score:", this_node.goal_score)
    