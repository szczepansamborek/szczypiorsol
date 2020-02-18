def solution(A):
    N = len(A)
    lp = 0
    for i in range(N):
        if i > A[i]:
            lp += A[i]
        else:
            lp += i
        for j in range(A[i]):
            if i + j < N:
                if j > A[i + j]:
                    lp += 1
        if lp > 10000000:
            return -1
    return lp

print(solution([1, 5, 2, 1, 4, 0]))
print(solution([3, 1, 2, 2, 5, 6]))
print(solution([0, 0, 0, 0, 0, 0]))
