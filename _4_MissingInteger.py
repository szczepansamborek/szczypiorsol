def solution(A):
    B = []
    for i in A:
        if i > 0 and i <= 100000:
            B.append(i)
    if len(B) == 0:
        return 1
    B.sort()
    for i in range(len(B) - 1):
        if B[i] < B[i + 1] - 1:
            return B[i] + 1
    return B[-1] + 1

print(1)
print(5)
print(solution([1, 3, 6, 4, 1, 2]))
print(2)
print(4)
print(solution([1, 2, 3]))
print(3)
print(1)
print(solution([-1, -3]))
