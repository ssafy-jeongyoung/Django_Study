def bfs(row, col):
    queue = [(row, col)]
    visited[row][col] = 1
    while queue:
        cr, cc = queue.pop(0)
        for k in range(4):
            nr, nc = cr + di[k], cc + dj[k]
            if 1 <= nr < N+1 and 1 <= nc < M+1 and lab[nr][nc] == 0 and not visited[nr][nc]:
                lab[nr][nc] = 2
                visited[nr][nc] = 1
                queue.append((nr, nc))


def solve(count, lab, idx):
    global max_v
    if len(space)-idx < count:
        return

    if count == 0:
        for s in range(len(virus)):
            vr, vc = virus[s]
            bfs(vr, vc)
        value = 0
        for a in range(1, N+1):
            for b in range(1, M+1):
                if lab[a][b] == 0:
                    value += 1
        if value > max_v:
            max_v = value
        return

    for s in range(idx, len(space)):
        ci, cj = space[s]
        solve(count, lab, s+1)
        lab[ci][cj] = 1
        solve(count-1, lab, s+1)
        lab[ci][cj] = 0
    return


N, M = map(int, input().split())

lab = [[1]*(M+2)] + [[1] + list(map(int, input().split())) + [1] for _ in range(N)] + [[1]*(M+2)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
visited = [[0]*(M+2) for _ in range(N+2)]
virus = []
space = []

for i in range(1, N+1):
    for j in range(1, M+1):
        if lab[i][j] == 2:
            virus.append((i, j))
        elif lab[i][j] == 0:
            space.append((i, j))
print(virus)
print(space)
max_v = 0
solve(3, lab, 0)
print(max_v)