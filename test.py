import numpy as np

a = np.array([1,2,3])

print(a)

x = np.arange(4).reshape(2,2)
print(x)

y = np.zeros((5,6),dtype=int)
print(y)

number = y[1]

print(number)

y[1,2] = 100

print(y[1,2])



'''
values = [[0,0],[0,0]]
values[0][0] = 1
values[0][1] = 1
print(values[0])
if values[0] == [1,1]:
    print("yes")



rows, cols = (5, 5) 
arr = [[0]*cols]*rows 
print(arr) 
'''