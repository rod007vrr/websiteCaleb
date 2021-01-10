from Classes.tree import Node
from Classes.exercise import Exercise
from Classes.person import Person

#Constructing body tree
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
        



workoutData = [line for line in open(r"website\wktAnalysis\body.txt", 'r')]

testPerson = Person(1)



