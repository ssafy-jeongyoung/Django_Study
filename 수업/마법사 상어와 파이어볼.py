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

field = [[0, 0, 0, 0] * N for _ in range(N)]
for i in range(M):
    field[fire_ball[0]-1][fire_ball[1]-1] = [1, fire_ball[2], fire_ball[3], fire_ball[4]]

for k in range(K):
    