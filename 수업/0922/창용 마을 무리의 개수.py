# x, y 노드를 하나의 집합으로 만들어주기
# x가 포함된 집합과 y가 포함된 집합을 하나의 집합으로 만들기
def union(x, y):
    # 1. 이미 같은 집합인 지 체크
    x = find_set(x)
    y = find_set(y)

    # 대표자가 같으니, 같은 집합이다.
    if x == y:
        return

    # 2. 다른 집합이라면, 같은 대표자로 수정
    if x < y:
        person[y] = x
    else:
        person[x] = y


# x가 포함된 집합의 대표자를 반환하는 함수
# x가 어떤 집합에 포함되었는지 확인하는 함수
def find_set(x):
    #대표자는 노드번호와 부모노드번호가 일치하는 노드
    if x == person[x]:
        return x
    # 스스로가 대표자가 아니면...몰라..>>> 부모에게 물어보기
    person[x] = find_set(person[x])
    return person[x]


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    person = [x for x in range(N+1)]

    for i in range(M):
        a, b = map(int, input().split())
        union(a, b)
    print(person)
    s = set()
    for i in range(1, N+1):
        s.add(person[i])
    print(f'#{tc} {len(s)}')