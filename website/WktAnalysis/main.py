from Classes.exercise import Exercise
from Classes.person import Person

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

test = Person(0)

test.stats.printTree()

test.updateStats()