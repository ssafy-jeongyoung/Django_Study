a, b = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

AtoB = []
BtoA = []

for i in A:
    if i not in B:
        AtoB.append(i)

for i in B:
    if i not in A:
        BtoA.append(i)

print(len(AtoB)+len(BtoA))