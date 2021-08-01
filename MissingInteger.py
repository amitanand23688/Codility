'''
Write a function:

    def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

        N is an integer within the range [1..100,000];
        each element of array A is an integer within the range [−1,000,000..1,000,000].

'''
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    c = 1
    if len(A)>1:
        A.sort()
        if max(A) < 0:
            return 1
        for i in range(0, len(A)):
            if A[i] == c:
                c += 1
            elif A[i] < c:
                pass
            elif A[i] > c:
                return c
        return i+2
    return 1
