import math

def solution(A, B, K):
    if A % K == 0:
        d = K
    else:
        d = A % K
    return math.floor((B - A + d) / K)


print(solution(6, 11, 2))
print(solution(3, 45, 5))
