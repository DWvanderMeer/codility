def solution(A,K):
    if not len(A):
        return A
    for k in range(K):
        x = A[-1]
        A.pop(-1)
        A.insert(0, x)
    return(A)