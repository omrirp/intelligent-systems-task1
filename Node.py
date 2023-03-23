class Node:
    def __init__(self, cell, i, j, parent=None):
        self.cell = cell
        self.i = i
        self.j = j
        self.parent = parent

    def getParent(self):
        return self.parent