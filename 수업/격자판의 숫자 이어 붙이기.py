di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


def solve(cnt, row, col, su):

    if cnt == 8:
        if su not in case:
            case.append(su)
        return

    for k in range(4):
        ni = row + di[k]
        nj = col + dj[k]
        if 0 <= ni < 4 and 0 <= nj < 4:
            solve(cnt+1, ni, nj, su+field[ni][nj])


T = int(input())

for tc in range(1, T+1):
    field = [list(input().split()) for _ in range(4)]
    case = []

    for i in range(4):
        for j in range(4):
            val = field[i][j]
            solve(2, i, j, val)

    print(f'#{tc} {len(case)}')