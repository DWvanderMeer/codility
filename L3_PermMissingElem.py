A = [2, 3, 1, 5]

def solution(A):
    n = len(A)
    B = [i for i in range(1,n+2)]
    s = set(B)-set(A)
    return(list(s)[0])

########################################################################################
# Test copied from https://github.com/johnmee/codility/blob/master/L3_PermMissingElem.py
# Test passed.
########################################################################################
