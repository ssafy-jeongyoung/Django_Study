def merge_sort(arr, n):
    global ans2
    if len(arr) == 1:
        return arr
    if n % 2 != 0:
        arr1 = merge_sort(arr[:n//2], n//2)
        arr2 = merge_sort(arr[n//2:], n//2+1)
    else:
        arr1 = merge_sort(arr[:n // 2], n // 2)
        arr2 = merge_sort(arr[n // 2:], n // 2)

    if arr1[-1] > arr2[-1]:
        ans2 += 1
    new_arr = []
    while arr1 or arr2:
        if arr1 and arr2:
            if arr1[0] > arr2[0]:
                new_arr.append(arr2.pop(0))
            elif arr1[0] <= arr2[0]:
                new_arr.append(arr1.pop(0))
        elif arr1:
            new_arr.append(arr1.pop(0))
        elif arr2:
            new_arr.append(arr2.pop(0))
    return new_arr


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    ans2 = 0
    ans = merge_sort(lst, N)

    print(f'#{tc} {ans[N//2]} {ans2}')