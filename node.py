import copy

class Node:
    counter = 0
    def __init__(self, pos, mat, parent=None, dir=None):
        self.row = pos[0]
        self.col = pos[1]
        self.pos = pos
        self.content = mat[self.row][self.col]
        self.parent = parent
        self.id = Node.counter
        Node.counter += 1
        self.agent_score=0
        self.goal_score=0
        self.dir=dir
        self.g=0
        self.cost=None
        # if self.get_op()=='a' or self.get_op()=='-':
        #     self.cost=1
        # elif self.get_op()=='b' or self.get_op=='+':
        #     self.cost=2
        # elif self.get_op()=='*':
        #     self.cost=5
        # elif self.get_op()=='**':
        #     self.cost=11
        # elif self.node.get_op()=='g':
        #     self.cost=1
        
        if self.parent:
            self.visited_nodes = copy.deepcopy(self.parent.visited_nodes)
            self.depth=self.parent.depth+1
            # self.h=self.parent.h+self.cost
        else:
            self.visited_nodes = []
            self.depth=0
            # self.h=0

        self.visited_nodes.append(self.pos)

        


    def get_opt(self):
        return self.content[0].lower()

    def get_number(self):
        return int(self.content[1:])
