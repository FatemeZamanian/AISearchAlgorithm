from os import path
from sklearn import neighbors
from node import Node

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


def read_testCase(file):
    fle=open(file)
    bf=fle.read()
    mat=[]
    rows=bf.split('\n')
    r,c=rows[0].split(' ')
    for i,row in enumerate(rows):
        if i !=0:
            mat.append(row.split(' '))
    return mat,int(r),int(c)


def find_root(mat,r,c):
    for i in range(int(r)):
        for j in range(int(c)):
            if 's' in (mat[i][j].lower()):
                return (i,j)

def find_goal(mat,r,c):
    for i in range(int(r)):
        for j in range(int(c)):
            if 'g' in (mat[i][j].lower()):
                return (i,j)


def get_opt(mat,r, c):
    return mat[r][c][0].lower()

def get_number(mat,r,c):
    return int(mat[r][c][1:])


def set_op(mat,r,c,score,goal_score):
    op= get_opt(mat,r,c)
    if op=='+':
        score+=get_number(mat,r,c)
    if op=='-':
        score-=get_number(mat,r,c)
    if op=='*':
        score*=get_number(mat,r,c)
    if op=='a':
        goal_score+=get_number(mat,r,c)
    if op=='b':
        goal_score-=get_number(mat,r,c)
    return score,goal_score


def find_neighbors(node,score,goal_score,path):
    mat,r,c=read_testCase('test-case/2.txt')
    cells=[]
    if node.row>0 and get_opt(mat,node.row - 1, node.col) != 'w':
        n=Node(node.row-1,node.col,mat[node.row-1][node.col],(node.row,node.col))
        if (n.row,n.col) not in path:
            score,goal_score=set_op(mat,n.row,n.col,score,goal_score)
            cells.append(n)
    if node.row<r-1 and get_opt(mat,node.row + 1, node.col) != 'w':
        n=Node(node.row+1,node.col,mat[node.row+1][node.col],(node.row,node.col))
        if (n.row,n.col) not in path:
            score,goal_score=set_op(mat,n.row,n.col,score,goal_score)
            cells.append(n)
    if node.col>0 and get_opt(mat,node.row, node.col-1) != 'w':
        n=Node(node.row,node.col-1,mat[node.row][node.col-1],(node.row,node.col))
        if (n.row,n.col) not in path:
            score,goal_score=set_op(mat,n.row,n.col,score,goal_score)
            cells.append(n)
    if node.col<c-1 and get_opt(mat,node.row, node.col+1) != 'w':
        n=Node(node.row,node.col+1,mat[node.row][node.col+1],(node.row,node.col))
        if (n.row,n.col) not in path:
            score,goal_score=set_op(mat,n.row,n.col,score,goal_score)
            cells.append(n)
    return cells,score,goal_score






def bfs(mat,r,c):
    root=find_root(mat,r,c)
    goal=find_goal(mat,r,c)
    goal_score=get_number(mat,goal[0],goal[1])
    rr=root[0]
    rc=root[1]
    start=mat[rr][rc]
    now=(rr,rc,start)
    score=get_number(mat,rr,rc)
    path=[(rr,rc)]
    q=[]
    q.append(Node(root[0],root[1],start,'root'))
    while len(q)>0:
        now=q.pop(0)
        neighbors,score,goal_score=find_neighbors(now,score,goal_score,path)
        for c in neighbors:
            print((c.row,c.col))
            if c.row==goal[0] and c.col==goal[1]:
                # if get_number(mat,goal[0],goal[1])<score:
                print('find')
                print((c.row,c.col))
                # print(path)
                # print(score)
                return
            else:
                if (c.row,c.col) not in path:
                    path.append((c.row,c.col))
                    q.append(c)
    # print(goal_score)
    print(score)
    # print(path)

        # for i in range(r):
        #     for j in range(c):
        #         if i==rr or j==rc:
        #             if get_opt(mat,i,j).lower()=='g':
        #                 path.append((i,j))
        #                 print('find')
        #                 return
        #             elif 'w' not in (mat[i][j].lower()) and (i,j) not in path:
        #                 path.append((i,j))
        #                 print(i,j)
        #                 q.append(Node(i,j,mat[i][j],now))
        #                 score,goal_score=set_op(mat,i,j,score,goal_score)
                        
        # rr=now.row
        # rc=now.col
        # print(score)
        



        # for i in range(r):
        #     for j in range(c):
        #         if i==rr or j==rc:
        #             if get_opt(mat,i,j).lower()=='g':
        #                 print(mat)
        #                 path.append((i,j))
        #                 print(path)
        #                 print(score)
        #                 succes=True
        #             if 'w' not in (mat[i][j].lower()) and (i,j) not in path:
        #                 # neighbors.append(Node(i,j,mat[i][j],now))
        #                 now=(mat[i][j],i,j)
        #                 rr=i
        #                 rc=j
        #                 score,goal_score=set_op(mat,i,j,score,goal_score)
        #                 path.append((i,j))
        #                 print(now)
                        

mat,r,c=read_testCase('test-case/1.txt')
bfs(mat,r,c)
