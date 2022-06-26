
a = [ [ (-1,-1) for i in range(3) ] for j in range(3 + 1) ]

a[0][0] = (1,12)
prev = (0,0)
a[prev[0]][prev[1]] = (-1,-5)
for i in range(len(a)):
    print(a[i])

