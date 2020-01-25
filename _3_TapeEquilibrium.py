def solution(A):
    # write your code in Python 3.6
    s1 = A[0]
    s2 = sum(A) - A[0]
    sMin = abs(s1 - s2)
    for i in range(1, len(A)):
        s1 += A[i]
        s2 -= A[i]
        sTemp = abs(s1 - s2)
        if sTemp < sMin:
            sMin = sTemp
    return sMin

print(1)
print(1)
print(solution([3, 1, 2, 4, 3]))
