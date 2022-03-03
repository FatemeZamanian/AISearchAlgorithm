from treelib import Tree
from utils import find_root,find_goal,find_neighbors,print_tree,print_path
from node import Node
import time
def bds(mat):
    start_pos = find_root(mat)
    goal_pos = find_goal(mat)
    goal = Node(goal_pos, mat,dir='l')
    start = Node(start_pos, mat,dir='r') # No parent means its the root node
    visited=[]
    start.agent_score = start.get_number()+goal.get_number()
    start.goal_score = goal.get_number()
    q = []
    q.append(start)
    q.append(goal)
    while len(q) > 0:
        for i in q:
            print(i.pos,i.dir)
        this_node = q.pop(0)
        # print(this_node.pos,this_node.dir)
        
        if this_node.pos not in visited:
            neighbors = find_neighbors(mat,this_node,this_node.dir)
            for neighbor in neighbors:
                print(neighbor.pos,neighbor.dir)
                if neighbor.pos in this_node.visited_nodes and this_node.dir != neighbor:
                    # if neighbor.agent_score > neighbor.goal_score:
                    print("Found")
                    print("agent score:", neighbor.agent_score)
                    print("goal score:", neighbor.goal_score)
                    return
                
                else:
                    if neighbor.pos not in this_node.visited_nodes:
                        q.append(neighbor)
        else:
            visited.append(this_node.pos)
        time.sleep(1)
            
    print("Not found")
    print("agent score:", this_node.agent_score)
    print("goal score:", this_node.goal_score)
    