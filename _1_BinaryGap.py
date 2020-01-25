def solution(N):
    # write your code in Python 3.6
    strN = "{0:b}".format(N)
    print(strN)
    maxGap = 0
    gap = 0
    for i in strN:
        if i == '1':
            if gap > maxGap:
                maxGap = gap
            gap = 0
        else:
            gap += 1
    return maxGap

print(solution(1041))
print(solution(562378))
print(solution(5729))
print(solution(98177))
print(solution(32))
print(solution(1))
print(solution(7))
print(solution(87529572))
print(solution(1850297324))
