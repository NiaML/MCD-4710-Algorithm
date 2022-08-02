from sys import float_info
from math import pi

# Student details
def details():
    student_number = '' #write your student number as a string
    student_email = '' + '@student.monash.edu' #write your student email
    name = '' #write your name as it appears on Moodle
    return str(student_number), student_email, name


# Task 1
def swap(lst, a, b):
    """
    >>> family = ['Ransom', 'Linda', 'Walt', 'Joni']
    >>> swap(family, 3, 2)
    >>> family
    ['Ransom', 'Linda', 'Joni', 'Walt']
    """
    pass


def find_min(lst, index):
    """
    >>> find_min(['candlestick', 'pipe', 'rope', 'knife', 'wrench'], 2)
    3
    >>> find_min([1, 3, 5, 11, 7, 3, 2, 6, 2], 3)
    6
    """
    pass


# Selection sort
def selection_sort(lst):
    """
    >>> outsiders = ['Marta', 'Edi', 'Frank', 'Benoit']
    >>> selection_sort(outsiders)
    >>> outsiders
    ['Benoit', 'Edi', 'Frank', 'Marta']
    """
    pass
        

# Task 2
def swap_down(lst, j):
    """
    >>> shawshank = ['Andy', 'Red', 'Tommy', 'Brooks']
    >>> swap_down(shawshank, 2)
    >>> shawshank
    ['Andy', 'Red', 'Tommy', 'Brooks']
    >>> swap_down(shawshank, 3)
    >>> shawshank
    ['Andy', 'Red', 'Brooks', 'Tommy']
    """
    pass


def shuffle_down(lst, k):
    """
    >>> club = ['Ben', 'Eddie', 'Bill', 'Richie', 'Stanley', 'Beverly', 'Mike']
    >>> shuffle_down(club, 5)
    >>> club
    ['Ben', 'Beverly', 'Eddie', 'Bill', 'Richie', 'Stanley', 'Mike']
    """
    pass


def insertion_sort(lst):
    """
    >>> hawkins = ['Mike', 'Eleven', 'Dustin', 'Lucas', 'Will']
    >>> insertion_sort(hawkins)
    >>> hawkins
    ['Dustin', 'Eleven', 'Lucas', 'Mike', 'Will']
    """
    pass


# Task 3
def degree(graph, v):
    """
    >>> friends = [[0, 1, 1, 1, 0],
    ...            [1, 0, 0, 0, 0],
    ...            [1, 0, 0, 1, 1],
    ...            [1, 0, 1, 0, 1],
    ...            [0, 0, 1, 1, 0]]
    >>> degree(friends, 0)
    3
    >>> degree(friends, 1)
    1
    >>> degree(friends, 4)
    2
    """
    pass


def shared_friends(graph, u, v):
    """
    >>> friends = [[0, 1, 1, 1, 0],
    ...            [1, 0, 0, 0, 0],
    ...            [1, 0, 0, 1, 1],
    ...            [1, 0, 1, 0, 1],
    ...            [0, 0, 1, 1, 0]]
    >>> shared_friends(friends, 0, 4)
    [2, 3]
    """
    pass


def are_friends(graph, u, v):
    """
    >>> friends = [[0, 1, 1, 1, 0],
    ...            [1, 0, 0, 0, 0],
    ...            [1, 0, 0, 1, 1],
    ...            [1, 0, 1, 0, 1],
    ...            [0, 0, 1, 1, 0]]
    >>> are_friends(friends, 0, 4)
    False
    >>> are_friends(friends, 0, 1)
    True
    """
    pass


def clique(graph, vertices):
    """
    >>> friends = [[0, 1, 1, 1, 0],
    ...            [1, 0, 0, 0, 0],
    ...            [1, 0, 0, 1, 1],
    ...            [1, 0, 1, 0, 1],
    ...            [0, 0, 1, 1, 0]]
    >>> clique(friends, [2, 3, 4])
    True
    >>> clique(friends, [0, 1, 2])
    False
    """
    pass


# Task 4 (Extension: Not Assessed)
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


if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)