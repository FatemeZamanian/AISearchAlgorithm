from utils import *

def calc_toatal_cost():
    pass


def a_star(mat):
    start_pos = find_root(mat)
    goal_pos = find_goal(mat)

    goal = Node(goal_pos, mat)
    start = Node(start_pos, mat) # No parent means its the root node
    
    start.agent_score = start.get_number()
    start.goal_score = goal.get_number()

    q = []
    q.append(start)
    while len(q) > 0:
        min=q[0]
        for i in range(len(q)):
            if q[i].h<min.h:
                min=q[i]
                min_index=i
        this_node = q.pop(min_index)
        neighbors = find_neighbors(mat,this_node)
        for neighbor in neighbors:
            if neighbor.pos == goal.pos:
                if neighbor.agent_score > neighbor.goal_score:
                    print("Found")
                    print("agent score:", neighbor.agent_score)
                    print("goal score:", neighbor.goal_score)
                    print_path(neighbor)
                    return
            else:
                if neighbor.pos not in this_node.visited_nodes:
                    q.append(neighbor)

    print("Not found")
    print("agent score:", this_node.agent_score)
    print("goal score:", this_node.goal_score)
    


