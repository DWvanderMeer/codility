
def solution(A):
    test_triangle = lambda P, Q, R: (P + Q > R) and (Q + R > P) and (R + P > Q)
    A = sorted(A)
    for i in range(len(A) - 2):
        if test_triangle(A[i], A[i+1], A[i+2]):
            return(1)
    return(0)


#################################################################################
# Test copied from https://github.com/johnmee/codility/blob/master/L6_Triangle.py
# Test passed and scales well.
#################################################################################
