from node import Node
def find_root(mat):
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if 's' in (mat[i, j].lower()):
                return [i, j]

def find_goal(mat):
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if 'g' in (mat[i, j].lower()):
                return [i, j]


def set_op(this_node, neighbor):
    opt = neighbor.get_opt()
    neighbor.agent_score = this_node.agent_score
    neighbor.goal_score = this_node.goal_score

    if opt=='+':
        neighbor.agent_score += neighbor.get_number()
    elif opt=='-':
        neighbor.agent_score -= neighbor.get_number()
    elif opt=='*':
        neighbor.agent_score *= neighbor.get_number()
    elif opt == '^':
        neighbor.agent_score **= neighbor.get_number()
    elif opt=='a':
        neighbor.goal_score += neighbor.get_number()
    elif opt=='b':
        neighbor.goal_score -= neighbor.get_number()


def find_neighbors(mat,this_node:Node):
    neighbors = []

    # مختصات خانه هایی که احتمالا همسایه باشند
    neighbors_candidate_pos = [
        [this_node.row-1, this_node.col],
        [this_node.row, this_node.col-1],
        [this_node.row+1, this_node.col],
        [this_node.row, this_node.col+1]
    ]

    for pos in neighbors_candidate_pos:
        if 0 <= pos[0] < mat.shape[0] and 0 <= pos[1] < mat.shape[1]:  # اگر مختصات همسایه معتبر بود
            neighbor = Node(pos, mat, parent=this_node)
            if neighbor.get_opt() != 'w':                
                set_op(this_node, neighbor)
                neighbors.append(neighbor)
        
    return neighbors


def print_path(goal):
    # حرکت از پایین به بالا
    # حرکت از هدف به سمت ریشه
    print("Path")
    this_node = goal
    print(this_node.pos)
    while this_node.parent != None:
        this_node = this_node.parent
        print(this_node.pos)
    print()

def print_tree(tree):
    tree.show()