from Classes.tree import Node
from Classes.exercise import Exercise
from Classes.person import Person

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

#Constructing exercises
with open(r"exercises.txt", 'r') as file: #!change filename
    data = [line for line in file]
    
exercises = []

currentExerciseName = ""
currentExerciseTargetIntensityPairs = {}

for n in data:
    if n == "\n":
        exercises.append(Exercise(currentExerciseName, currentExerciseTargetIntensityPairs))
    elif not n.startswith("    "):
        currentExerciseName = n.strip(":")
    else:
        pair = n.split(":")
        currentExerciseTargetIntensityPairs[pair[0].strip()] = int(pair[1].strip())

#Testing for individual person

test = Person(0, deepCopy(bodyTree))
