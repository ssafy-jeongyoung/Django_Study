di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

def bfs(row, col):
    global num
    queue = [(row, col)]
    visited[row][col] = 1

    while queue:
        cr, cc = queue.pop(0)
        for k in range(4):
            nr, nc = cr + di[k], cc + dj[k]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and area[nr][nc] != 0:
                queue.append((nr, nc))
                visited[nr][nc] = 1

    num += 1
    return

N = int(input())

area = [list(map(int, input().split())) for _ in range(N)]
max_height = 0
for i in area:
    max_height = max(max_height, max(i))
ans = 0
for n in range(max_height+1):
    for i in range(N):
        for j in range(N):
            if area[i][j] <= n:
                area[i][j] = 0

    num = 0
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and area[i][j] != 0:
                bfs(i, j)
    if num > ans:
        ans = num
print(ans)