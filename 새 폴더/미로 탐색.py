def bfs(row, col):
    global ans
    stack = [(row, col)]
    visited[row][col] = 1
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    while stack:
        cr, cc = stack.pop(0)

        for k in range(4):
            nr, nc = cr + di[k], cc + dj[k]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and miro[nr][nc] != '0':
                visited[nr][nc] = visited[cr][cc] + 1
                stack.append((nr, nc))




N, M = map(int, input().split())

miro = [input() for _ in range(N)]
visited = [[0]*M for _ in range(N)]

bfs(0, 0)
print(visited[N-1][M-1])