from math import sqrt, pi
from sys import float_info
import random # For task1c
import timeit # For task1c
'''
DO NOT CHANGE THE NAME OF THIS FILE, or else the tester will not work. 
The first function requires that you replace the given strings with
your personal details. It is important that you enter your student number
and your student email correctly. If your number and email do not match we
will then check your name, so your name acts as a failsafe.
'''

# Student details
def details():
    student_number = '33191654' #write your student number as a string
    student_email = 'clam0049' + '@student.monash.edu' #write your student email
    name = 'Chi Him Lam' #write your name as it appears on Moodle
    return str(student_number), student_email, name


# Task 1A - Merge
def merge(lst1, lst2):
    """
    Input: Two sorted lists lst1, lst2
    Output: One sorted list 'res' merged together
    >>> merge([1, 2, 4, 6], [3, 5, 7, 8])
    [1, 2, 3, 4, 5, 6, 7, 8]

    >>> merge([1, 2, 3], [4, 5, 6])
    [1, 2, 3, 4, 5, 6]

    >>> merge([11, 13, 15], [])
    [11, 13, 15]

    >>> merge([], [16, 18, 20])
    [16, 18, 20]
    """
    index_1 = 0
    index_2 = 0
    res = []
    while index_1 < len(lst1) and index_2 < len(lst2):
        if lst1[index_1] <= lst2[index_2]:
            res.append(lst1[index_1])
            index_1+=1
        else:
            res.append(lst2[index_2])
            index_2+=1
    for i in (lst1[index_1:], lst2[index_2:]):
        # join the rest from the lists
        res.extend(i)
            
    
    return res
    

    pass


# Task 1B - Merge Sort
def merge_sort(lst):
    """
    Input: list of elements
    Output: Sorted list of elements
    >>> merge_sort([3, 7, 9, 6, 2, 5, 4, 1, 8])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    >>> merge_sort([11, 0, 1, 5, 7, 2])
    [0, 1, 2, 5, 7, 11]

    >>> merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    # perform merge sort
    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst)//2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        return merge(left, right)
    pass


# Task 1C - Analysis of Sorting Algorithms
def sort_analysis(func, n):
    """
    Input: The sort function as an argument and 'n' which represents the
           no. of elements of the input lists you will create.
    Output: A dictionary of the sorting order (i.e., keys) and times (i.e., values)
            for the specific sort.

    ANALYSIS: <WRITE YOUR PARAGRAPH HERE>
    """
    
    pass



# Task 2 - Post Offices
def dist(p1, p2):
    """Computes Eucledian distance between points p1 and p2.
    """
    import math

    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    pass


def offices_to_merge(points):
    """
    Input : list of 2d coordinates of post offices,
            points=[(x1, y1), (x2, y2)...(xn, yn)]} with n>1
    Output: a pair of indices (l, k) such that...
            for all pairs of indices 0 <= i < j <=n it holds that
            dist(points[l], points[k]) <= dist(points[i], points[j])
    
    For example:
    >>> points = [(350, 150), (500, 250), (150, 150), (50, 400), (200,100)]
    >>> offices_to_merge(points)
    (2, 4)
    """
    pass


# Task 3 - Regula Falsi: Extension (OPTIONAL)
def sign(x):
    pass
    
def root(f, a, b, acc=float_info.min):
    """
    Input : continuous function f, floats a, b, and acc
            such that the signs of f(a) and f(b) differ
    Output: float x such that abs(f(x))<=acc

    For example:
    >>> from math import log, isclose
    >>> isclose(root(log, 0.1, 2), 1.0)
    True
    >>> def p(x): return 1-x**2
    >>> isclose(root(p, -2, 0), -1.0)
    True
    >>> isclose(root(p, 0, 100), 1.0)
    True
    >>> from math import sin, pi, isclose
    >>> isclose(root(sin, 1, 4), pi)
    True
    """
    pass


# Task 1C - Analysis of Sorting Algorithms
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
