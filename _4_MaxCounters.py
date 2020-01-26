def solution(N, A):
    W = [0] * N
    for i in A:
        if i == N + 1:
            W = [max(W)] * N
        else:
            W[i - 1] += 1
    return W

print(1)
print([3, 2, 2, 4, 2])
print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
