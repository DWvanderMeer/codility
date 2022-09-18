
def solution(A):
    if not A:
        return(0)
    B = [i for i in range(1,len(A)+1)]
    if len(set(B) - set(A)) == 0:
        return(1)
    else:
        return(0)

#print(solution([4, 1, 3, 2]))
#print(solution([4, 1, 3]))
#print(solution([2]))
#print(solution([1]))
#print(solution([]))

##################################################################################
# Test copied from https://github.com/johnmee/codility/blob/master/L4_PermCheck.py
# Test passed.
##################################################################################