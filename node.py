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
        
        
        if self.parent:
            self.visited_nodes = copy.deepcopy(self.parent.visited_nodes)
            self.depth=self.parent.depth+1
        else:
            self.visited_nodes = []
            self.depth=0

        self.visited_nodes.append(self.pos)


    def get_opt(self):
        return self.content[0].lower()

    def get_number(self):
        return int(self.content[1:])


class NodeA(Node):
    def __init__(self, pos, mat, parent=None, dir=None):
        super().__init__(pos, mat, parent, dir)
        self.g=0
        if self.parent :
            self.h=self.parent.h+self.set_cost()
        else:
            self.h=0
    
    def set_cost(self):
        op=self.content[0].lower()
        if op=='a' or op=='-':
            self.cost=1
        elif op=='b' or op=='+':
            self.cost=2
        elif op=='*':
            self.cost=5
        elif op=='**':
            self.cost=11
        elif op=='g':
            self.cost=1
        else:
            self.cost=0
        return self.cost
    
    


