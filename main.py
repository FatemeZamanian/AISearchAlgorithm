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


def succes(mat,r,c):
    gr,gc=find_goal(mat,)


def bfs(mat,r,c):
    root=find_root(mat,r,c)
    goal=find_goal(mat,r,c)
    rr=root[0]
    rc=root[1]
    start=mat[rr][rc]
    now=(rr,rc,start)
    score=get_number(mat,rr,rc)
    goal_score=get_number(mat,goal[0],goal[1])
    path=[]
    q=[]
    q.append(Node(root[0],root[1],start,'root'))
    while len(q)>0:
        now=q.pop(0)
        print(now.row,now.col,now.value)
        for i in range(r):
            for j in range(c):
                if i==rr or j==rc:
                    if get_opt(mat,i,j).lower()=='g':
                        path.append((i,j))
                        print('find')
                        return
                    elif ((i,j)) not in path:
                        path.append((i,j))
                        q.append(Node(i,j,mat[i][j],now))
        return
        rr=now.row
        rc=now.col
        
        print(path)



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
                        

mat,r,c=read_testCase('test-case/2.txt')
bfs(mat,r,c)
