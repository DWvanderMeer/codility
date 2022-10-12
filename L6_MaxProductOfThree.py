
def solution(A):
    A = sorted(A)
    return(max(A[0]*A[1]*A[-1], A[-3]*A[-2]*A[-1]))

##########################################################################################
# Test copied from https://github.com/johnmee/codility/blob/master/L6_MaxProductOfThree.py
# Test passed and scales well.
##########################################################################################
