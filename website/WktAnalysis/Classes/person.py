class Person:
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
                
    def __init__(self, UUID): #! Change this function to take the paths to the exercises as inputs
        self.UUID = UUID
        
        #Constructing body tree
        with open(r"body.txt", 'r') as file: #!change filename
            data = [str(line.replace("    ", "?")).strip() for line in file]
        self.bodyTree = Person.Node({data[0]: 0})
        del data[0]
        currentRoot = self.bodyTree
        for part in data:
            if part.count("?") > list(currentRoot.data.keys())[0].count("?"):
                currentRoot.insert(Person.Node({part.strip("?"): 0}))
            elif part.count("?") <= list(currentRoot.data.keys())[0].count("?"):
                currentRoot = Person.Node({part.strip("?"): 0})
        
        self.stats = currentRoot
        
        #Constructing exercises
        with open(r"exercises.txt", 'r') as file: #!change filename
            data = [line for line in file]
            
        self.exercises = {}
        tempName = ""
        tempPairs = {}
        
        for n in data:
            if n == "\n":
                self.exercises[tempName[:-2]] = tempPairs
                tempName = ""
                tempPairs = {}
            elif not n.startswith("    "):
                tempName = n.strip(":")
            else:
                pair = n.split(":")
                tempPairs[pair[0].strip()] = int(pair[1].strip())

    def updateStats(self, workout):
        
        
        def processExercise(exercise, reps):
            for bpName, bpAmount in self.exercises[exercise].items():
                updateSpec(self.bodyTree ,bpName, bpAmount*reps)
                
        def updateSpec(source ,name, amount):

            
            try:
                source.data[name] += amount
            except:
                pass
            
            for n in source.subNodes:
                try:
                    n.data[name] += amount
                    for x in n.subNodes:
                        x.data
                        
                except:
                    pass
                
                        
                
                
            
            
        
        with open(workout, 'r') as file:
            data = [line for line in file]
            
        for n in data:
            splitD = n.split(":")
            processExercise(splitD[0].strip(), int(splitD[1]))
   