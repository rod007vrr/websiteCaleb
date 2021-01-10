from tree.tree import Node

with open(r"website\wktAnalysis\body.txt", 'r') as file:
    data = [str(line.replace("    ", "?")).strip() for line in file]
    
root = Node(data[0])
del data[0]

currentRoot = root

for part in data:
    if part.count("?") > currentRoot.data.count("?"):
        currentRoot.insert(Node(part.strip("?")))
    elif part.count("?") <= currentRoot.data.count("?"):
        currentRoot = Node(part.strip("?"))
        

root.printTree()