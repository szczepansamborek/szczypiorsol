def solution(A):
    # write your code in Python 3.6
    A.sort()
    for i in range(len(A)):
        if A[i] != i + 1:
            return i + 1
    return len(A)

print(1)
print(4)
print(solution([2, 3, 1, 5]))
