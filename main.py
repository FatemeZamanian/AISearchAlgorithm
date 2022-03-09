import numpy as np
import argparse
from treelib import Tree

from bfs import bfs
from dfs import dfs
from dls import dls
from ids import ids
from bds import bds
from Astar import a_star
from idAstar import id_a_star


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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--file-path", default="test-case/3.txt")
    parser.add_argument("--algorithm", default="a*")
    args = parser.parse_args()
    mat = read_testCase(args.file_path)
    if args.algorithm=="bfs":
        bfs(mat)
    elif args.algorithm=="dfs":
        dfs(mat)
    elif args.algorithm=="ids":
        ids(mat)
    elif args.algorithm=="bds":
        bds(mat)
    elif args.algorithm=="a*":
        a_star(mat)
    elif args.algorithm=="ida*":
        id_a_star(mat)
    else:
        print('algorithm not found ')   
