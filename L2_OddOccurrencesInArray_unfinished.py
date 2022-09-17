'''
A non-empty array A consisting of N integers is given. The array contains an odd number 
of elements, and each element of the array can be paired with another element that has 
the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

def solution(A)
that, given an array A consisting of N integers fulfilling the above conditions, returns 
the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.
'''
import unittest
import random
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

class TestOddOccurencesInArray(unittest.TestCase):

    MAX_N = 1000000  # Max value in the array.
    MAX_A = 1000000000  # Max length of the array.

    @staticmethod
    def gen_array(L, odd):
        """Generate a list of sample data: random integers in pairs.
        :param L: the length of the list is double this int
        :param odd: the odd integer out
        * Generate a list of random ints half the size required.
        * Join it to a duplicate of itself.
        * Append the odd value.
        * Shuffle the array and return.
        """
        arr = []
        for _ in range((L - 1) // 2):
            val = random.randint(1, TestOddOccurencesInArray.MAX_N)
            arr.extend((val, val))
        arr.append(odd)
        random.shuffle(arr)
        return arr

    def test_sample_generation(self):
        print(self.gen_array(5, 1))

    def test_example1(self):
        arr = [9, 3, 9, 3, 9, 7, 9]
        self.assertEqual(7, solution(arr))

    def test_simple1(self):
        """simple test n=5"""
        arr = self.gen_array(5, 4)
        self.assertEqual(4, solution(arr))

    def test_simple2(self):
        """simple test n=11"""
        arr = self.gen_array(11, 4)
        self.assertEqual(4, solution(arr))

    def test_extreme_single_item(self):
        """list containing one item"""
        self.assertEqual(42, solution([42]))

    def test_small1(self):
        """small random test n=201"""
        arr = self.gen_array(201, 42)
        self.assertEqual(42, solution(arr))
    
    def test_small2(self):
        """small random test n=601"""
        arr = self.gen_array(601, 4242)
        self.assertEqual(4242, solution(arr))

    def test_medium1(self):
        """medium random test n=2001"""
        arr = self.gen_array(2001, 100)
        self.assertEqual(100, solution(arr))
    
    def test_medium2(self):
        """medium random test n=100,003"""
        arr = self.gen_array(100003, 500000)
        self.assertEqual(500000, solution(arr))
    '''
    def test_big1(self):
        """big random test n=999,999, multiple repetitions"""
        arr = self.gen_array(100003, 700)
        self.assertEqual(700, solution(arr))

    def test_big2(self):
        """big random test n=999,999"""
        arr = self.gen_array(999999, 5000111222)
        self.assertEqual(5000111222, solution(arr))
    '''

if __name__ == '__main__':
    unittest.main()