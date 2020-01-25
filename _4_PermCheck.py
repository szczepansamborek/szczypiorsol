def solution(A):
    # write your code in Python 3.6
    s = set(A)
    print(s)
    if len(s) != len(A):
        return 0
    elif max(s) == len(A):
        return 1
    else:
        return 0

print(1)
print(1)
print(solution([4, 1, 3, 2]))
print(2)
print(0)
print(solution([4, 1, 3]))
