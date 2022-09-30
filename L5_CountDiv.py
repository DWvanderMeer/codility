
def solution(A, B, K):
    count = 0
    for i in range(A,B+1):
        if i%K==0:
            count+=1
    return(count)

#################################################################################
# Test copied from https://github.com/johnmee/codility/blob/master/L5_CountDiv.py
# Tests passed although it doesn't scale well.
#################################################################################