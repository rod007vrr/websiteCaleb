tl = [1,2,3,4,5,6,7,8,9, 34, 3453, 345234234]
print(tl)
tlS = str(tl)
print(tlS)
nut = [int(n) for n in tlS.removeprefix("[").removesuffix("]").split(",")]
print(nut)