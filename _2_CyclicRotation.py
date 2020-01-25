def solution(A, K):
    # write your code in Python 3.6
    N = len(A)
    r = N - K
    while r < 0:
        r += N
    W = []
    for i in range(N):
        W.append(A[(r + i) % N])
    return W

print(1)
print([9, 7, 6, 3, 8])
print(solution([3, 8, 9, 7, 6], 3))
print(2)
print([3, 8, 9, 7, 6])
print(solution([3, 8, 9, 7, 6], 0))
print(3)
print([7, 6, 3, 8, 9])
print(solution([3, 8, 9, 7, 6], -3))
print(4)
print([3, 8, 9, 7, 6])
print(solution([3, 8, 9, 7, 6], 5))
print(5)
print([3, 8, 9, 7, 6])
print(solution([3, 8, 9, 7, 6], -5))
print(6)
print([6, 3, 8, 9, 7])
print(solution([3, 8, 9, 7, 6], 6))
print(7)
print([8, 9, 7, 6, 3])
print(solution([3, 8, 9, 7, 6], -6))
