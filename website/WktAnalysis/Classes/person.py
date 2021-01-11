class Person:
    class Node:
        def __init__(self, data):
            self.data = data
            self.subNodes = []
            
        def insert(self, node):
            self.subNodes.append(node)
     
    class Exercise(object):
        def __init__(self, name, targetedIntensity):
            self.name = name
            self.targetedIntensity = targetedIntensity
        def print(self):
            print(f"\n{self.name}", end="")
            for n in self.targetedIntensity.items():
                print(n) 
     
                
    def __init__(self, UUID):
        self.UUID = UUID
        
        #Constructing body tree
        with open(r"body.txt", 'r') as file: #!change filename
            data = [str(line.replace("    ", "?")).strip() for line in file]
        bodyTree = Person.Node({data[0]: 0})
        del data[0]
        currentRoot = bodyTree
        for part in data:
            if part.count("?") > list(currentRoot.data.keys())[0].count("?"):
                currentRoot.insert(Person.Node({part.strip("?"): 0}))
            elif part.count("?") <= list(currentRoot.data.keys())[0].count("?"):
                currentRoot = Person.Node({part.strip("?"): 0})
        
        self.stats = currentRoot
        
    def updateStats(workout):
        """Updates stats with workout

        Args:
            workout ([string]): [file path to workout.txt]
        """
        def processExercise(exercise, reps):
            for n in exercise:
                pass
            
        
        
        with open(workout, 'r') as file:
            data = [line for line in file]
            
        for n in data:
            splitD = n.split(":")
            processExercise(splitD[0].strip(), int(splitD[1]))
            
            
            
            