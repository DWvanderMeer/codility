'''
An array A consisting of N different integers is given. The array contains 
integers in the range [1..(N + 1)], which means that exactly one element 
is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)
that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
'''

import unittest
import random

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

class TestExercise(unittest.TestCase):

    INT_RANGE = (0, 100000)

    def test_example1(self):
        self.assertEqual(solution([2, 3, 1, 5]), 4)

    def test_single(self):
        self.assertEqual(solution([2]), 1)
        self.assertEqual(solution([1]), 2)

    def test_random(self):
        arr = [n for n in range(1, random.randint(*self.INT_RANGE))]
        missing = random.randint(0, len(arr))
        arr.remove(missing)
        self.assertEqual(solution(arr), missing)

    def test_maximum(self):
        arr = [n for n in range(1, self.INT_RANGE[1] + 1)]
        arr.pop()
        self.assertEqual(solution(arr), self.INT_RANGE[1])


if __name__ == "__main__":
    unittest.main()