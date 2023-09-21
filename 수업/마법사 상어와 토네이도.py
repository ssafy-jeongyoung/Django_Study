# 좌로 이동 중일 때, 모래가 이동하는 방향
di_left = [0, 2, -2, 1, -1, -1, 1, 1, -1, 0]
dj_left = [-2, 0, 0, -1, -1, 1, 1, 0, 0, -1]
#          5%  2% 2% 10% 10% 1% 1% 7% 7% 55%

# 아래로 이동 중일 때, 모래가 이동하는 방향
di_bot = [2, 0, 0, 1, 1, -1, -1, 0, 0, 1]
dj_bot = [0, -2, 2, -1, 1, -1, 1, -1, 1, 0]
#         5% 2% 2% 10% 10% 1% 1% 7% 7% 55%

# 우로 이동 중일 때, 모래가 이동하는 방향
di_right = [0, 2, -2, -1, 1, -1, 1, 1, -1, 0]
dj_right = [2, 0, 0, 1, 1, -1, -1, 0, 0, 1]
      #     5% 2% 2% 10% 10% 1% 1% 7% 7% 55%

# 위로 이동 중일 때, 모래가 이동하는 방향
di_top = [-2, 0, 0, -1, -1, 1, 1, 0, 0, -1]
dj_top = [0, -2, 2, -1, 1, -1, 1, -1, 1, 0]
#        5%  2% 2% 10% 10% 1% 1% 7% 7% 55%
# ------------------------------------------------------------------------ #


N = int(input())
morae = [list(map(int, input().split())) for _ in range(N)]

mid = N // 2
# 필드 밖으로 나간 모래의 양 (정답)
ans = 0

# 토네이도의 위치
x = mid
y = mid

flag = 0   # 0 : 좌 ->  1: 하  ->  2: 우  ->  3: 상  -> 0 : 좌
move = 1   # 토네이도가 한 방향으로 이동하는 양
cnt = 0    # 방향 전환을 2번 하면 move가 1씩 증가

# 빙글 빙글 도는 토네이도~~
while True:
    # 토네이도를 도는 코드 구현  -> flag를 이용해 4개 상하좌우 방향 전환
    # 이동 시 모래 이동 및 모래 더하기 구현  -> di dj 사용
    # 모래가 밖으로 나갔을 때 나간 양 더하기 구현  -> ni, nj가 범위 밖이면 더해줌

    if flag == 0:   # 좌로 이동!
        for i in range(move):
            x, y = x, y-1
            origin = morae[x][y]
            for k in range(10):
                ni = x + di_left[k]
                nj = y + dj_left[k]
                if k == 0:  # 5% 이동
                    morae[x][y] -= int(origin / 20)
                    # 모래가 밖으로 안 나갈 때
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += int(origin / 20)
                    # 모래가 밖으로 나갈 때
                    else:
                        ans += int(origin / 20)

                elif k == 1 or k == 2:  # 2% 이동
                    morae[x][y] -= int(origin / 50)
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += int(origin / 50)
                    else:
                        ans += int(origin / 50)

                elif k == 3 or k == 4:  # 10% 이동
                    morae[x][y] -= int(origin / 10)
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += int(origin / 10)
                    else:
                        ans += int(origin / 10)

                elif k == 5 or k == 6:  # 1% 이동
                    morae[x][y] -= int(origin / 100)
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += int(origin / 100)
                    else:
                        ans += int(origin / 100)

                elif k == 7 or k == 8:  # 7% 이동
                    morae[x][y] -= int((origin * 7) / 100)
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += int((origin * 7) / 100)
                    else:
                        ans += int((origin * 7) / 100)

                else:  # 55% 이동
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += morae[x][y]
                    else:
                        ans += morae[x][y]
            morae[x][y] = 0

        if x == 0 and y == 0:
            break
        # 2번 방향 전환하면 move 1증가
        cnt += 1
        if cnt == 2:
            if move < N - 1:
                move += 1
            cnt = 0
        # 좌로 이동 끝나면 하로 이동
        flag = 1

    elif flag == 1:   # 하로 이동!
        for i in range(move):
            x, y = x+1, y
            origin = morae[x][y]
            for k in range(10):
                ni = x + di_bot[k]
                nj = y + dj_bot[k]
                if k == 0:  # 5% 이동
                    morae[x][y] -= int(origin / 20)
                    # 모래가 밖으로 안 나갈 때
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += int(origin / 20)
                    # 모래가 밖으로 나갈 때
                    else:
                        ans += int(origin / 20)

                elif k == 1 or k == 2:  # 2% 이동
                    morae[x][y] -= int(origin / 50)
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += int(origin / 50)
                    else:
                        ans += int(origin / 50)

                elif k == 3 or k == 4:  # 10% 이동
                    morae[x][y] -= int(origin / 10)
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += int(origin / 10)
                    else:
                        ans += int(origin / 10)

                elif k == 5 or k == 6:  # 1% 이동
                    morae[x][y] -= int(origin / 100)
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += int(origin / 100)
                    else:
                        ans += int(origin / 100)

                elif k == 7 or k == 8:  # 7% 이동
                    morae[x][y] -= int((origin * 7) / 100)
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += int((origin * 7) / 100)
                    else:
                        ans += int((origin * 7) / 100)

                else:  # 55% 이동
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += morae[x][y]
                    else:
                        ans += morae[x][y]
            morae[x][y] = 0
        # 2번 방향 전환하면 move 1증가
        cnt += 1
        if cnt == 2:
            if move < N - 1:
                move += 1
            cnt = 0
        # 하로 이동 끝나면 우로 이동
        flag = 2

    elif flag == 2:   # 우로 이동!
        for i in range(move):
            x, y = x, y+1
            origin = morae[x][y]
            for k in range(10):
                ni = x + di_right[k]
                nj = y + dj_right[k]
                if k == 0:  # 5% 이동
                    morae[x][y] -= int(origin / 20)
                    # 모래가 밖으로 안 나갈 때
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += int(origin / 20)
                    # 모래가 밖으로 나갈 때
                    else:
                        ans += int(origin / 20)

                elif k == 1 or k == 2:  # 2% 이동
                    morae[x][y] -= int(origin / 50)
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += int(origin / 50)
                    else:
                        ans += int(origin / 50)

                elif k == 3 or k == 4:  # 10% 이동
                    morae[x][y] -= int(origin / 10)
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += int(origin / 10)
                    else:
                        ans += int(origin / 10)

                elif k == 5 or k == 6:  # 1% 이동
                    morae[x][y] -= int(origin / 100)
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += int(origin / 100)
                    else:
                        ans += int(origin / 100)

                elif k == 7 or k == 8:  # 7% 이동
                    morae[x][y] -= int((origin * 7) / 100)
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += int((origin * 7) / 100)
                    else:
                        ans += int((origin * 7) / 100)

                else:  # 55% 이동
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += morae[x][y]
                    else:
                        ans += morae[x][y]
            morae[x][y] = 0
        # 2번 방향 전환하면 move 1증가
        cnt += 1
        if cnt == 2:
            if move < N-1:
                move += 1
            cnt = 0
        # 우로 이동 끝나면 위로 이동
        flag = 3

    elif flag == 3:   # 위로 이동!
        for i in range(move):
            x, y = x-1, y
            origin = morae[x][y]
            for k in range(10):
                ni = x + di_top[k]
                nj = y + dj_top[k]
                if k == 0:  # 5% 이동
                    morae[x][y] -= int(origin / 20)
                    # 모래가 밖으로 안 나갈 때
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += int(origin / 20)
                    # 모래가 밖으로 나갈 때
                    else:
                        ans += int(origin / 20)

                elif k == 1 or k == 2:  # 2% 이동
                    morae[x][y] -= int(origin / 50)
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += int(origin / 50)
                    else:
                        ans += int(origin / 50)

                elif k == 3 or k == 4:  # 10% 이동
                    morae[x][y] -= int(origin / 10)
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += int(origin / 10)
                    else:
                        ans += int(origin / 10)

                elif k == 5 or k == 6:  # 1% 이동
                    morae[x][y] -= int(origin / 100)
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += int(origin / 100)
                    else:
                        ans += int(origin / 100)

                elif k == 7 or k == 8:  # 7% 이동
                    morae[x][y] -= int((origin * 7) / 100)
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += int((origin * 7) / 100)
                    else:
                        ans += int((origin * 7) / 100)

                else:  # 55% 이동
                    if 0 <= ni < N and 0 <= nj < N:
                        morae[ni][nj] += morae[x][y]
                    else:
                        ans += morae[x][y]

            morae[x][y] = 0
        # 2번 방향 전환하면 move 1증가
        cnt += 1
        if cnt == 2:
            if move < N - 1:
                move += 1
            cnt = 0
        # 위로 이동 끝나면 좌로 이동
        flag = 0

print(ans)