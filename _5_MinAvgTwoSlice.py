def solution(A):
    N = len(A)
    minAvg = max(A)
    minI = 0
    for i in range(N - 1):
        for j in range(1, N):
            if i < j:
                avg = sum(A[i : j + 1])/(j + 1 - i)
                if avg < minAvg:
                    minI = i
                    minAvg = avg
    return minI
                    
    

print(solution([4, 2, 2, 5, 1, 5, 8]))
