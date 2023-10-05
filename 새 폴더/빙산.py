from collections import deque

def bfs(row, col):
    global space
    dq = deque()
    dq.append((row, col))
    visited[row][col] = 1
    while dq:
        cr, cc = dq.popleft()
        for k in range(4):
            nr, nc = cr + di[k], cc + dj[k]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and not new_sea[nr][nc]:
                visited[nr][nc] = 1
                dq.append((nr, nc))
    space += 1
    return


N, M = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(N)]

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
space = 0


while space < 2:
    visited = [[0]*M for _ in range(N)]
    new_sea = [[0]*M for _ in range(N)]

    # 빙산 하나하나 얼마나 녹을지 확인
    for i in range(1, N-1):
        for j in range(1, M-1):
            if sea[i][j] != 0:
                cnt = 0  # 주변의 바다와 접촉한 면의 수
                for p in range(4):
                    ni, nj = i +di[p], j + dj[p]
                    if sea[ni][nj] == 0:
                        cnt += 1
                ice = sea[i][j] - cnt
                if ice < 0:
                    ice = 0
                new_sea[i][j] = ice

    # new_sea(1년이 지난 후의 빙산 배열) 완성
    # 이제 빙산이 몇 개인지 확인
    for i in range(N):
        for j in range(M):
            if new_sea[i][j] != 0 and not visited[i][j]:
                bfs(i, j)

    if space == 1:
        space = 0