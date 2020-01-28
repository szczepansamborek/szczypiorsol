def solution(S, P, Q):
    M = len(P)
    K = []
    for i in range(M):
        W = S[P[i]:Q[i] + 1]
        print(W)
        if W.count('A'):
            K.append(1)
        elif W.count('C'):
            K.append(2)
        elif W.count('G'):
            K.append(3)
        else:
            K.append(4)
    return K
        

print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))
