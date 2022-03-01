from os import path
from sklearn import neighbors
from torch import true_divide
from node import Node
import numpy as np
import argparse
from treelib import Tree


def get_matrix():
    rows=int(input('enter row: '))
    cols=int(input('enter col: '))
    mat=[]
    for r in range(rows):
        while True:
            x=input(f'enter row {r}:').split(' ')
            if len(x)==cols:
                mat.append(x)
                break
            else:
                print('wrong dim!!! \n Try again...')
    return mat


def read_testCase(file_path):
    f = open(file_path)
    rows_count, cols_count = f.readline().split(' ')
    rows_count = int(rows_count)
    cols_count = int(cols_count)
    mat=[]    
    for i in range(rows_count):
        mat.append(f.readline().rstrip().split(' '))  # rstrip removes \n
    
    mat = np.array(mat)
    return mat


def find_root():
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            if 's' in (mat[i, j].lower()):
                return [i, j]

def find_goal():
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


def find_neighbors(this_node:Node):
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


def bfs():
    # print(mat.shape)
    start_pos = find_root()
    goal_pos = find_goal()

    goal = Node(goal_pos, mat)
    start = Node(start_pos, mat) # No parent means its the root node
    
    start.agent_score = start.get_number()
    start.goal_score = goal.get_number()

    q = []
    q.append(start)
    while len(q) > 0:
        this_node = q.pop(0)

        if this_node.parent:
            tree.create_node(str(this_node.pos), str(this_node.id), parent=str(this_node.parent.id))
        else:
            tree.create_node(str(this_node.pos), str(this_node.id))  # No parent means its the root node 

        neighbors = find_neighbors(this_node)
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

def dfs():
    # print(mat.shape)
    start_pos = find_root()
    goal_pos = find_goal()

    goal = Node(goal_pos, mat)
    start = Node(start_pos, mat) # No parent means its the root node
    
    start.agent_score = start.get_number()
    start.goal_score = goal.get_number()

    q = []
    q.append(start)
    while len(q) > 0:
        this_node = q.pop(len(q)-1)

        if this_node.parent:
            tree.create_node(str(this_node.pos), str(this_node.id), parent=str(this_node.parent.id))
        else:
            tree.create_node(str(this_node.pos), str(this_node.id))  # No parent means its the root node 

        neighbors = find_neighbors(this_node)
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BFS")
    parser.add_argument("--file-path", default="test-case/1.txt")
    args = parser.parse_args()
    
    tree = Tree()
    mat = read_testCase(args.file_path)
    dfs()
    print("Tree")
    tree.show()
