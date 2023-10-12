from collections import deque


def bfs(row, col):
    dq = deque()
    dq.append((row, col))
    visited[row][col] = 1
    while dq:
        cr, cc = dq.popleft()
        for k in range(4):
            nr, nc = cr + di[k], cc + dj[k]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and new_sea[nr][nc] != 0:
                visited[nr][nc] = 1
                dq.append((nr, nc))


N, M = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
space = 0
ans = 0

while True:
    visited = [[0]*M for _ in range(N)]
    new_sea = [[0]*M for _ in range(N)]

    # 빙산 하나하나 얼마나 녹을지 확인
    for i in range(1, N-1):
        for j in range(1, M-1):
            if sea[i][j] != 0:
                cnt = 0  # 주변의 바다와 접촉한 면의 수
                for p in range(4):
                    ni, nj = i + di[p], j + dj[p]
                    if sea[ni][nj] == 0:
                        cnt += 1
                ice = sea[i][j] - cnt
                if ice < 0:
                    ice = 0
                new_sea[i][j] = ice
    # print(new_sea)
    ans += 1
    # new_sea(1년이 지난 후의 빙산 배열) 완성
    # 이제 빙산이 몇 개인지 확인
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and new_sea[i][j] != 0:
                bfs(i, j)
                space += 1
    # print(space)
    if space == 1:
        space = 0
        sea = new_sea[:]
        continue
    elif space > 1:
        break
    elif space == 0:
        ans = 0
        break
    # print(sea)
print(ans)