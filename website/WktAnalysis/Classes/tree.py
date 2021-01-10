class Node:
    def __init__(self, data):
        self.data = data
        self.subNodes = []
        
    def insert(self, node):
        self.subNodes.append(node)
        
    def printTree(self):
        print(self.data)
        for n in self.subNodes:
            n.printTree()