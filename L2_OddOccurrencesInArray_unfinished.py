#A = [9, 3, 9, 3, 9, 7, 9]

def solution(A):
    idx=[]
    for i in range(len(A)):
        if i in idx:
            continue
        for j in range(i+1,len(A)):
            if A[i]==A[j]:
                idx.append(i)
                idx.append(j)
                break
        
    B = [i for i in range(len(A))]
    idx_ = set(B) - set(idx)
    unpaired = A.pop(list(idx_)[0])
    return(unpaired)

#############################################################################################
# Test copied from https://github.com/johnmee/codility/blob/master/L2_OddOccurencesInArray.py
# Test passed although not the performance tests because of the nested for loop --> improve 
# w/ set operations.
#############################################################################################
