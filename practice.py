n = int(input())
M = [ ]
for i in range(n):
    row = [ ]
    for num in input().split(','):
        row.append(int(num))
    M.append(row)

some_var = 0
for i in range(n):
    for j in range(n):
        some_var += M[i][j]

print(some_var)