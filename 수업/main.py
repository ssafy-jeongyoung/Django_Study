# def merge_sort(arr):
#     if len(arr) == 1:
#         return arr
#     mid = len(arr) // 2
#     arr1 = arr[:mid]
#     arr2 = arr[min:]
#     new_arr = []
#
#     while arr1 and arr2:
#         if arr1[0] < arr2[0]:
#             new_arr.append(arr1.pop(0))
#         else:
#             new_arr.append(arr2.pop(0))
#
#         new_arr += arr1
#         new_arr += arr2
#         return


# def merge_sort2(arr):
#     s, e = 0, len(arr)-1
#     mid = (s+e)//2
#
#     i = s
#     j = mid + 1
#     tmp = []
#     while i <= mid and j <= e:
#         if arr[i] < arr[j]:
#             tmp.append(arr[i])
#             i += 1
#         else:
#             tmp.append(arr[j])
#             j += 1
#
#     while i <= mid:
#         tmp.append(arr[i])
#         i += 1
#
#     while j <= e:
#         tmp.append(arr[j])
#         j += 1
#     j = 0
#     for i in range(s, e+1):
#         arr[i] = tmp[j]
#         j += 1


def merge_sort3(arr, s, e):
    if s == e:
        return

    mid = (s + e) // 2

    merge_sort3(arr, s, mid)
    merge_sort3(arr, mid+1, e)

    i = s
    j = mid + 1
    tmp = []
    while i <= mid and j <= e:
        if arr[i] < arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    while i <= mid:
        tmp.append(arr[i])
        i += 1

    while j <= e:
        tmp.append(arr[j])
        j += 1
    j = 0
    for i in range(s, e + 1):
        arr[i] = tmp[j]
        j += 1

arr = [4, 3, 2, 10, 1, 5, 6, 8]
merge_sort3(arr, 0, len(arr)-1)
print(arr)