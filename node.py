class Node:
    counter = 0
    def __init__(self, pos, mat, parent=None):
        self.row = pos[0]
        self.col = pos[1]
        self.pos = pos
        self.content = mat[self.row][self.col]
        self.parent = parent
        self.id = Node.counter
        Node.counter += 1

    def get_opt(self):
        return self.content[0].lower()

    def get_number(self):
        return int(self.content[1:])
