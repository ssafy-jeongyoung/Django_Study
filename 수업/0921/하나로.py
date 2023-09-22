import math

def solve(start):
    MST = set()

    weight = [0xfffffff] * N
    weight[start] = 0
    while len(MST) < N-1:
        min_weight = 0xfffffff
        min_node = -1

        for k in range(N):
            if k not in MST and weight[k] < min_weight:
                min_weight = weight[k]
                min_node = k
        MST.add(min_node)
        print(MST)
        for k in range(N):
            if k not in MST and distance[min_node][k] < weight[k]:
                weight[k] = distance[min_node][k]
    return weight


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    island = [[0, 0] for _ in range(N)]
    for i in range(N):
        island[i][0] = X[i]
        island[i][1] = Y[i]

    distance = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(i+1, N):
            if i != j:
                d = math.sqrt((island[i][0]-island[j][0])**2 + (island[i][1]-island[j][1])**2)
                distance[i][j] = d
                distance[j][i] = d

    print(distance)
    adj = [0] * N
    lst = solve(0)
    ans = 0
    for i in range(N):
        ans += E *(lst[i]**2)

    print(f'#{tc} {round(ans)}')