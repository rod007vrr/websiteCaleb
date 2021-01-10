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

class Person(object):
    def __init__(self, UUID, stats):
        self.UUID = UUID
        self.stats = stats
        
        
        #Constructing body tree
        with open(r"body.txt", 'r') as file: #!change filename
            data = [str(line.replace("    ", "?")).strip() for line in file]
        bodyTree = Node({data[0]: 0})
        del data[0]

        currentRoot = bodyTree

        for part in data:
            if part.count("?") > list(currentRoot.data.keys())[0].count("?"):
                currentRoot.insert(Node({part.strip("?"): 0}))
            elif part.count("?") <= list(currentRoot.data.keys())[0].count("?"):
                currentRoot = Node({part.strip("?"): 0})