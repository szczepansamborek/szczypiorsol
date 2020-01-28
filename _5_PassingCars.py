def solution(A):
    s = 0
    j = 0
    for i in A:
        if i == 0:
            j += 1
        else:
            s += j
    return s

print(solution([0, 1, 0, 1, 1]))
