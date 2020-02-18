def solution(A):
    A.sort()
    if(A[0] * A[1] > A[-2] * A[-3] and A[-1] > 0):
        return A[0] * A[1] * A[-1]
    else:
        return A[-3] * A[-2] * A[-1]

print(solution([-3, 1, 2, -2, 5, 6]))
print(solution([-3, -1, -2, -2, -5, -6]))
print(solution([-3, -1, -2, -2, -5, 6]))
