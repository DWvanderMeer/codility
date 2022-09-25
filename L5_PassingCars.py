
def solution(A):
    lst = []
    for i in enumerate(range(len(A))):
        if(A[i]==0):
            lst.append(sum(A[i:]))
    if sum(lst) < 1000000000:
        return(sum(lst))
    else:
        return(-1)

####################################################################################
# Test copied from https://github.com/johnmee/codility/blob/master/L5_PassingCars.py
# Tests passed although not in terms of performance.
####################################################################################