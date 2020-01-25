def solution(X, A):
    # write your code in Python 3.6
    N = len(A)
    s = set()
    l = 0
    for i in range(N):
        if X - l > N - i:
            return -1
        s.add(A[i])
        l = len(s)
        if len(s) == X:
            return i
    return -1

print(1)
print(6)
print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
