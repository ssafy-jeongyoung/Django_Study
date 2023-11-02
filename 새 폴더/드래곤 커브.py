#     0   1  2  3 -> 0
di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]


def dragon_curve(col, row, direction, cnt):
    dragon_point[row][col] = 1
    before_direct = []

    count = 0
    while count < cnt:
        if not before_direct:
            before_direct.append(direction)
            next_row = row + di[direction]
            next_col = col + dj[direction]
            dragon_point[next_row][next_col] = 1
            row, col = next_row, next_col

        else:
            length = len(before_direct)
            for k in range(length-1, -1, -1):
                now_dir = before_direct[k]+1
                if now_dir == 4:
                    now_dir = 0
                next_row = row + di[now_dir]
                next_col = col + dj[now_dir]
                dragon_point[next_row][next_col] = 1
                row, col = next_row, next_col
                before_direct.append(now_dir)

        count += 1
    return


N = int(input())

dragon_point = [[0] * 101 for _ in range(101)]

for i in range(N):
    x, y, d, g = map(int, input().split())
    # print(x, y, d, g)
    dragon_curve(x, y, d, g+1)

ans = 0

for i in range(100):
    for j in range(100):
        if dragon_point[i][j] == 1 and dragon_point[i+1][j] == 1 and dragon_point[i][j+1] == 1 and dragon_point[i+1][j+1] == 1:
            ans += 1

print(ans)