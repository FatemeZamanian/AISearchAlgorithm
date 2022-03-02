from treelib import Tree
from utils import find_root,find_goal,find_neighbors,print_tree,print_path
from node import Node

def bds(mat):
    tree = Tree()
    # print(mat.shape)
    start_pos = find_root(mat)
    goal_pos = find_goal(mat)

    goal = Node(goal_pos, mat)
    start = Node(start_pos, mat) # No parent means its the root node
    
    start.agent_score = start.get_number()
    start.goal_score = goal.get_number()

    q = []
    q.append(start)
    q.append(goal)
    start.right_visited=True
    goal.left_visited=True
    while len(q) > 0:
        this_node = q.pop(0)

        # if this_node.parent:
        #     tree.create_node(str(this_node.pos), str(this_node.id), parent=str(this_node.parent.id))
        # else:
        #     tree.create_node(str(this_node.pos), str(this_node.id))  # No parent means its the root node 

        if this_node.left_visited and this_node.right_visited:
            if neighbor.agent_score > neighbor.goal_score:
                    print("Found")
                    print("agent score:", neighbor.agent_score)
                    print("goal score:", neighbor.goal_score)
                    tr=input('print tree?(y/n)')
                    if tr=='y':
                        print_tree(tree)
                    print_path(neighbor)
                    return

        neighbors = find_neighbors(mat,this_node)
        for neighbor in neighbors:
            if this_node.left_visited == True and not neighbor.left_visited:
                # neighbor.parent_left = this_node
                neighbor.left_visited = True
                q.append(neighbor)
            if this_node.right_visited == True and not neighbor.right_visited:
                # neighbor.parent_right = this_node
                neighbor.right_visited = True
                q.append(neighbor)

            
    print("Not found")
    print("agent score:", this_node.agent_score)
    print("goal score:", this_node.goal_score)
    