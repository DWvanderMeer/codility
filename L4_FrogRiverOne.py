
def solution(X, A):
    if len(A)==1 and A[0]>1:
        return(-1)
    B = [j for j in range(1,X+1)]
    tmp = []
    if not set(B)-set(A):
        for i in range(len(A)):
            if A[i] in B:
                tmp.append(A[i])
                if not set(B)-set(tmp):
                    return(i)
    else:
        return(-1)
print(solution(3, [2, 3, 1]))
print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))

#####################################################################################
# Test copied from https://github.com/johnmee/codility/blob/master/L4_FrogRiverOne.py
# Test passed except for the performance test which took too long.
#####################################################################################