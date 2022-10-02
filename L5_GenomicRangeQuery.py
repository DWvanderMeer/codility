
def l(letter):
    if letter == 'A':
        return 1
    elif letter == 'C':
        return 2
    elif letter == 'G':
        return 3
    elif letter == 'T':
        return 4

def solution(S, P, Q):
    lst = []
    for i in range(len(P)):
        s = S[P[i]:Q[i]+1]
        lst.append(l(sorted(s)[0]))
    return(lst)

##########################################################################################
# Test copied from https://github.com/johnmee/codility/blob/master/L5_GenomicRangeQuery.py
# Tests passed although it doesn't scale well for the last order of magnitude.
##########################################################################################
