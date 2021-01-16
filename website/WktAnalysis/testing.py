from Classes.person import Person
#Testing for individual person

test=Person()



data = [line for line in open(r"C:\Users\rod00\dev\website\websiteCaleb\website\WktAnalysis\workout.txt", 'r')]

test.updateStats(data)

print(test.bodyTree.printTree([]))


