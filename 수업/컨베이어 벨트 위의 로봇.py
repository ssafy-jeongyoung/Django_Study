N, K = map(int, input().split())

A = list(map(int, input().split()))
belt = [0] * (2*N)

ans = 0
robot = 1
while True:
    ans += 1

    # 과정 1
    belt.insert(0, belt.pop())
    A.insert(0, A.pop())
    # N-1의 위치에서는 로봇을 내려야 하므로 값을 0으로 만듬
    belt[N-1] = 0

    # 과정 2
    for i in range(N-2, -1, -1):
        if belt[i] != 0:
            if i == N-2:
                if A[i+1] > 0:
                    belt[i] = 0
                    A[i+1] -= 1
            else:
                if A[i+1] > 0 and belt[i+1] == 0:
                    belt[i+1] = belt[i]
                    belt[i] = 0
                    A[i+1] -= 1

    # 과정 3
    if A[0] > 0:
        belt[0] = robot
        A[0] -= 1
        robot += 1

    # 과정 4
    cnt = 0
    for i in range(2*N):
        if A[i] == 0:
            cnt += 1
    if cnt >= K:
        break

print(ans)

