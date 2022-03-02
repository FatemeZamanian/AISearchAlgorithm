from treelib import Tree
from utils import find_root,find_goal,find_neighbors,print_tree,print_path
from node import Node

def ids(mat,limit=0):
    tree = Tree()
    start_pos = find_root(mat)
    goal_pos = find_goal(mat)
    goal = Node(goal_pos, mat)
    start = Node(start_pos, mat) # No parent means its the root node
    
    start.agent_score = start.get_number()
    start.goal_score = goal.get_number()

    q = []
    q.append(start)
    while len(q) > 0:
        this_node = q.pop(0)
        # print(this_node.depth)
        

        if this_node.parent:
            tree.create_node(str(this_node.pos), str(this_node.id), parent=str(this_node.parent.id))
        else:
            tree.create_node(str(this_node.pos), str(this_node.id))  # No parent means its the root node 

        neighbors = find_neighbors(mat,this_node)
        for neighbor in neighbors:
            if neighbor.pos == goal.pos:
                if neighbor.agent_score > neighbor.goal_score:
                    print("Found")
                    print('limit: ',limit)
                    print("agent score:", neighbor.agent_score)
                    print("goal score:", neighbor.goal_score)
                    print_path(neighbor)
                    tr=input('print tree?(y/n)')
                    if tr=='y':
                        print_tree(tree)
                    return
            else:
                if neighbor.pos not in this_node.visited_nodes:
                    if neighbor.depth<=limit:
                        q.insert(0,neighbor)
    print('limit: ',limit)
    print("Not found")
    print("agent score:", this_node.agent_score)
    print("goal score:", this_node.goal_score)
    limit+=1
    ids(mat,limit)