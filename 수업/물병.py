def solve(n, k):
    c = 0
    while c <= k:
        c += n % 2
        n //= 2
        if n + c <= k:
            return True
    return False


N, K = map(int, input().split())
ans = 0
cnt = 0
while True:
    flag = solve(N, K)
    if flag:
        break
    else:
        if N % 2 == 0:
            N //= 2
        else:
            ans += 2**cnt
            N = N//2 + 1
    cnt += 1

print(ans)
