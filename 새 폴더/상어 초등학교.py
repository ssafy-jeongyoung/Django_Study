N = int(input())

classroom = [[0]*N for _ in range(N)]

in_student = set()
for p in range(N**2):
    s_num, like1, like2, like3, like4 = map(int, input().split())

    # 만약 좋아하는 학생이 이미 교실 안에 자리 잡고 있다면..
    if like1 in in_student or like2 in in_student or like3 in in_student or like4 in in_student:
        # 전체 순회하면서 좋아하는 사람이 인접한 칸에 가장 많은 곳에 착석
        # 순회 돌면서 최대값 갱신하면 그 칸의 위치도 같이 저장해두면 편할듯..

        pass
    # 좋아하는 학생이 교실 안에 없는 상태라면... 가장 인접한 빈 자리가 많은 곳에 앉음
    else:
        # 전체 순회 후 빈 칸이 가장 많은 곳에 착석
        max_cnt = 0
        point = None
        for i in range(N):
            for j in range(N):
                if classroom[i][j] == 0:
                    cnt = 0
                    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < N:
                            if classroom[ni][nj] == 0:
                                cnt += 1
                    if cnt == 4:   # 빈 칸이 4자리면 최대치이므로 바로 break
                        max_cnt = 4
                        point = (i, j)
                        break
                    elif cnt > max_cnt:
                        max_cnt = cnt
                        point = (i, j)
            if max_cnt == 4:
                break
        classroom[point[0]][point[1]] = s_num

    # 교실 안에 어떤 학생이 있는지 파악하기 위해 리스트에 학생번호 추가
    in_student.add(s_num)