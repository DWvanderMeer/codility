
def solution(A):
    n = len(A)
    diff = []
    for i in range(1,n):
        left = A[0:i]
        right = A[i:]
        diff.append(abs(sum(left)-sum(right)))
    return(min(diff))

########################################################################################
# Test copied from https://github.com/johnmee/codility/blob/master/L3_TapeEquilibrium.py
# Test passed although it could probably be enhanced in terms of performance
########################################################################################