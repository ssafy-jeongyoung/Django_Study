import math
N, M, K = map(int, input().split())
# 4*4, 파이어볼 2개, 이동횟수 1

fire_ball = [list(map(int, input().split())) for _ in range(M)]
# 1 1 5 2 2
# (1, 1) 질량 5, 이동칸 수 2, 방향 2
# 1 4 7 1 6
# (1, 4) 질량 7, 이동칸 수 1, 방향 6
# 답 : 8

# 파이어볼 방향
#     0   1  2  3  4  5   6   7
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

# 질량이 0이면 소멸
# 합쳐진 파이어볼 질량 = (m의 합)/5
# 합쳐진 파이어볼 속력 = (s의 합)/(파이어볼 갯수)
# 합쳐진 파이어볼 방향 = 모두 홀수 or 모두 짝수이면 0,2,4,6 // 아니면 1,3,5,7

field = [[[None]] * N for _ in range(N)]
# print(field)

for i in range(M):
    if field[fire_ball[i][0]-1][fire_ball[i][1]-1] == [None]:
        field[fire_ball[i][0]-1][fire_ball[i][1]-1] = [(True, fire_ball[i][2], fire_ball[i][3], fire_ball[i][4])]
    else:
        field[fire_ball[i][0] - 1][fire_ball[i][1] - 1].append((True, fire_ball[i][2], fire_ball[i][3], fire_ball[i][4]))


while K > 0:
    # 과정 1 : 파이어볼 1회 이동 시키기
    for i in range(N):
        for j in range(N):
            if field[i][j] != [None]:
                # 한 위치에 파이어볼이 단 하나일 때...
                if len(field[i][j]) == 1 and field[i][j][0][0] == True:
                    #               방향           속력
                    ni = i + di[field[i][j][0][3]] * field[i][j][0][2]
                    if ni < 0 or ni >= N:
                        ni %= N
                    nj = j + dj[field[i][j][0][3]] * field[i][j][0][2]
                    if nj < 0 or nj >= N:
                        nj %= N
                    if field[ni][nj] == [None]:
                        field[ni][nj] = [(False, field[i][j][0][1], field[i][j][0][2], field[i][j][0][3])]
                    else:
                        field[ni][nj].append((False, field[i][j][0][1], field[i][j][0][2], field[i][j][0][3]))
                    field[i][j] = [None]
                # 한 위치에 파이어볼이 여러 개 일 때...
                elif len(field[i][j]) > 1:
                    for k in range(len(field[i][j])):
                        if field[i][j][k][0] == True:
                            ni = i + di[field[i][j][k][3]] * field[i][j][k][2]
                            if ni < 0 or ni >= N:
                                ni %= N
                            nj = j + di[field[i][j][k][3]] * field[i][j][k][2]
                            if nj < 0 or nj >= N:
                                nj %= N

                            if field[ni][nj] == [None]:
                                field[ni][nj] = [(False, field[i][j][k][1], field[i][j][k][2], field[i][j][k][3])]
                            else:
                                field[ni][nj].append((False, field[i][j][k][1], field[i][j][k][2], field[i][j][k][3]))
                    field[i][j] = [None]

    # 과정 1-1. 이동해서 False가 된 거 다 True로 바꿔주기. 단, 파이어볼이 하나만 있는 것만 바꾸면 됨
    # 여러 개 있는 경우 합치면서 True 넣어주면 됨
    for i in range(N):
        for j in range(N):
            if field[i][j] != [None] and len(field[i][j]) == 1:
                field[i][j] = [(True, field[i][j][0][1], field[i][j][0][2], field[i][j][0][3])]

    # # 과정 2. 2개 이상 있으면 합치고 나누기
    for i in range(N):
        for j in range(N):
            if field[i][j] != [None] and len(field[i][j]) > 1:
                sum_m = 0  # 질량
                sum_s = 0  # 속력
                sum_d = []  # 방향
                for k in range(len(field[i][j])):
                    sum_m += field[i][j][k][1]
                    sum_s += field[i][j][k][2]
                    sum_d.append(field[i][j][k][3])
                # 속력 질량 나누기
                sum_m = math.floor(sum_m / 5)
                sum_s = math.floor(sum_s / len(field[i][j]))
                print(sum_s)
                # 방향 정하기
                if sum_d[0] % 2 == 0:  # 첫 방향이 짝수일 때...
                    even_flag = True
                    for p in sum_d:
                        if i % 2 != 0:
                            even_flag = False
                            break
                    if even_flag:
                        sum_d = [0, 2, 4, 6]
                    else:
                        sum_d = [1, 3, 5, 7]
                else:                  # 홀수일 때...
                    odd_flag = True
                    for p in sum_d:
                        if i % 2 != 1:
                            odd_flag = False
                            break
                    if odd_flag:
                        sum_d = [0, 2, 4, 6]
                    else:
                        sum_d = [1, 3, 5, 7]
                field[i][j] = [(True, sum_m, sum_s, sum_d[0]), (True, sum_m, sum_s, sum_d[1]), (True, sum_m, sum_s, sum_d[2]), (True, sum_m, sum_s, sum_d[3])]
    # while문 종료 카운트
    K -= 1

ans = 0
for i in range(N):
    for j in range(N):
        if field[i][j] != [None] and len(field[i][j]) == 1:
            ans += field[i][j][0][1]
        elif field[i][j] != [None] and len(field[i][j]) > 1:
            for k in range(len(field[i][j])):
                ans += field[i][j][k][1]

print(ans)