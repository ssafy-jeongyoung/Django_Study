X = int(input())
lst = [64]


while sum(lst) > X:
    stick = sum(lst)

    if stick > X:
        lst[-1] //= 2
        lst.append(lst[-1]) #  32 32
        if sum(lst) - lst[-1] >= X:
            lst.pop()


print(len(lst))