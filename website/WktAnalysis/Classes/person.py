class Person:
    class Node:
        def __init__(self, data, head):
            self.data = data
            self.subNodes = []
            self.head = head
            ''' add in a path to the the root node
            while root != None:
                [] #make an optional header argument so that it can call back to there
            '''
        def insert(self, node):
            self.subNodes.append(node)
            
        def getHead(self):
            return self.head
        def getSubnodes(self):
            return self.subNodes
            
        def printTree(self):
            print(self.data)
            for n in self.subNodes:
                n.printTree() 
                
    def __init__(self, UUID): #! Change this function to take the paths to the exercises as inputs
        self.UUID = UUID
        
        #Constructing body tree
        with open(r"body.txt", 'r') as file: #!change filename
            data = [str(line.replace("    ", "?")).strip() for line in file]
        self.bodyTree = Person.Node({data[0]: 0}, None)
        del data[0]
        currentRoot = self.bodyTree
        
        for item in data:
            if item.count("?") > list(currentRoot.data.keys())[0].count("?"):
                temp = Person.Node({item:0}, currentRoot)
                currentRoot.insert(temp)
                currentRoot = temp
            elif item.count("?") == list(currentRoot.data.keys())[0].count("?"):
                temp = Person.Node({item:0}, currentRoot.head)
                currentRoot.head.insert(temp)
                currentRoot = temp
            elif item.count("?") < list(currentRoot.data.keys())[0].count("?"):
                current = currentRoot
                while item.count("?") - list(current.data.keys())[0].count("?") != 1:
                    current = current.getHead()
                temp = Person.Node({item: 0}, current)
                current.insert(temp)
                currentRoot = temp
                
        def clearQ(node):
            if list(node.data.keys())[0] == "Body":
                pass
            else:
                node.data[list(node.data.keys())[0].strip("?")] = 0
                del node.data[list(node.data.keys())[0]]
            for subNode in node.subNodes:
                clearQ(subNode)
        
        clearQ(self.bodyTree)
                
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
                updateSpec(self.bodyTree, bpName, bpAmount*reps)
        
        def updateAll(node, amount):
            node.data[list(node.data.keys())[0]] = self.amount
            
            for subNode in node.subNodes:
                updateAll(subNode, self.amount)
                
                
        def updateSpec(tree, name, amount):
            self.amount = amount
            for n in tree.getSubnodes():
                try:
                    n.data[name] += amount
                    updateAll(n, amount)
                except KeyError:
                    pass
                updateSpec(n, name, amount)
                
        with open(workout, 'r') as file:
            data = [line for line in file]
            
        for n in data:
            splitD = n.split(":")
            processExercise(splitD[0].strip(), int(splitD[1]))
   