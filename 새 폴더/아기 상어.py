from collections import deque

# 필요합 로직
# 1. 먹을 수 있는 물고기 판별하는 코드
# 2.

di = [-1, 0, 0, 1]
dj = [0, -1, 1, 0]

def bfs(s, e, now_size):

    dq = deque()
    dq.append((s, e))

    visited = [[0]*N for _ in range(N)]
    visited[s][e] = 1
    while dq:
        ci, cj = dq.popleft()
        # 만약 현재 위치의 물고기 크기가 자신보다 작으면 먹이 후보 등록 : (거리, 행, 열)
        if 0 < space[ci][cj] < now_size:
            food.append((visited[ci][cj] - 1, ci, cj))

        # 만약 현재 위치의 거리가 food에 저장된 거리보다 멀다면 종료
        if food and visited[ci][cj] - 1 > food[0][0]:
            break

        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and space[ni][nj] <= now_size:
                dq.append((ni, nj))
                visited[ni][nj] = visited[ci][cj] + 1
    # print(food)
    return

N = int(input())

space = [list(map(int, input().split())) for _ in range(N)]
baby_shark_size = 2

point = deque()
# 처음 상어의 위치 확인 --------------------------------------------------
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            point.append((i, j))
            break
    if point:
        break

# 잡아먹을 수 있는 시간,  구해야 할 정답 -----------------------------------
count = 0
evolution_cnt = 0

# 잡아먹으로 이동 -------------------------------------------------------
while True:
    food = deque()
    # print(point)
    # print(count, baby_shark_size, evolution_cnt)
    si, sj = point.pop()
    bfs(si, sj, baby_shark_size)
    if not food:
        break
    else:
        # print(food)
        # print(food[0][0])
        # print()
        d, ei, ej = N**2, N, N
        l = len(food)
        for y in range(l):
            food_d, food_ei, food_ej = food.popleft()
            if food_d <= d:
                if food_ei < ei:
                    d, ei, ej = food_d, food_ei, food_ej
                elif food_ei == ei:
                    if food_ej < ej:
                        d, ei, ej = food_d, food_ei, food_ej
        count += d
        space[si][sj] = 0
        space[ei][ej] = 9
        evolution_cnt += 1
        if evolution_cnt == baby_shark_size and baby_shark_size < 8:
            baby_shark_size += 1
            evolution_cnt = 0
        point.append((ei, ej))
    # print(space)
print(count)