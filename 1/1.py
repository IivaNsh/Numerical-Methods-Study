#suppose matix is quadratic

# matrix
a = [
    [5, 3, 47, 1],
    [1, 0.2, 3, 1],
    [-1, 1, 0, 2],
    [1, 0, 124, -2]
]

# rigth hand side
b = [2,1,-4,4]

# x to find
x = [0,0,0,0]

N = len(a)
for i in range(N):
    el = a[i][i]
    for j in range(i+1,N):
        el2 = a[j][i]
        f = el2/el
        for k in range(N):
            a[j][k] -= a[i][k]*f
        b[j] -= b[i]*f
        
for i in range(N)[::-1]:
    r = b[i]
    for j in range(N-1, i, -1):
        r -= a[i][j]*x[j]
    x[i] = r/a[i][i]
    #//print(i)

for row,v in zip(a,b):
    print(*map(lambda x: "{:10.3f}".format(x), [*row,v]))

print()
print(*map(lambda x: "{:10.3f}".format(x), x))