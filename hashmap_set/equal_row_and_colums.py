grid = [[3,2,1],[1,7,6],[2,7,7]]
rows = len(grid)
cols = len(grid[0])
transpose_grid = [[0 for _ in range(cols)] for _ in range(rows)]


for i in range(len(grid)):
    for j in range(len(grid[0])):
        transpose_grid[j][i] = grid[i][j]
ans = 0
for i in range(len(grid)):
    for j in range(len(transpose_grid)):
        if grid[i] == transpose_grid[j]:
            ans+=1
print(ans)
