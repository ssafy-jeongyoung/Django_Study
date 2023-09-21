def lomuto_partition(left, right):
    pivot = arr[right]
    # i = 작은 요소들을 추적
    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # 피벗 위치 교환
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    # 피벗의 새 위치를 반환
    return i + 1


def quick_sort(left, right):
    if left < right:
        pivot = lomuto_partition(left, right)
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0, N-1)
    print(f'#{tc} {arr[N//2]}')
    