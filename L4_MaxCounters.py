
def solution(N, A):
    res = [0 for i in range(N)]
    for i in range(len(A)):
        if A[i] <= N:
            res[A[i]-1] = res[A[i]-1]+1
        elif A[i] == N+1:
            res = [max(res) for j in range(N)]
    return(res)

####################################################################################
# Test copied from https://github.com/johnmee/codility/blob/master/L4_MaxCounters.py
# Test passed although it could probably be enhanced in terms of performance
####################################################################################