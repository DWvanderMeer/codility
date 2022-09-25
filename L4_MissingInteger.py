
def solution(A):
    S = [i for i in range(1,max(A)+1)]
    S_ = set(S) - set(A)
    if len(S_)>0:
        return(min(list(S_)))
    elif len(S_)==0 and max(A)>0:
        return(max(A)+1)
    elif len(S_)==0 and max(A)<0:
        return(1) 

#######################################################################################
# Test copied from https://github.com/johnmee/codility/blob/master/L4_MissingInteger.py
# Tests passed although not in terms of performance.
#######################################################################################