def per(idx):
    global max_v
    if idx == N:
        # print(tmp)
        ans = ''
        for j in range(len(tmp)):
            ans += tmp[j]
        # print(int(ans))
        if int(ans) > B :
            return
        if max_v < int(ans):
            max_v = int(ans)
            return

    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            tmp[idx] =A[i]
            per(idx+1)
            used[i] = 0




A,B = input().split()
B = int(B)
# A순열 만들기 -> C가 됨
# 가능한 C 중 B보다 작으면서 가장큰값 구하기 , 없으면 -1
# C 는 0으로 시작할 수 없음

N = len(A)
tmp = [0] * N
used = [0] * N
max_v = 0
per(0)
print(max_v)