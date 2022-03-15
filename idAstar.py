from utils import *
from node import *
    

def id_a_star(mat):
    start_pos = find_root(mat)
    goal_pos = find_goal(mat)

    goal = NodeA(goal_pos, mat)
    start = NodeA(start_pos, mat) # No parent means its the root node
    
    start.agent_score = start.get_number()
    start.goal_score = goal.get_number()
    
    f_limit = 10

    q = []
    q.append(start)
    while True:
        while len(q) > 0:
            min_cost = q[0].g + q[0].h
            min_index = -1
            for i in range(len(q)):
                cost = q[i].g + q[i].h
                if cost <= min_cost and cost <= f_limit:
                    min_cost = cost
                    min_index = i

            if min_index == -1:
                break
            this_node = q.pop(min_index)

            neighbors = find_neighbors(mat,this_node)
            for neighbor in neighbors:
                if neighbor.pos == goal.pos:
                    if neighbor.agent_score > neighbor.goal_score:
                        print("Found")
                        print("f limit:", f_limit)
                        print("agent score:", neighbor.agent_score)
                        print("goal score:", neighbor.goal_score)
                        print_path(neighbor)
                        return
                else:
                    if neighbor.pos not in this_node.visited_nodes:
                        q.append(neighbor)

        print("Not found")
        print("f limit:", f_limit)
        print("agent score:", this_node.agent_score)
        print("goal score:", this_node.goal_score)
    
        f_limit = min_cost
    