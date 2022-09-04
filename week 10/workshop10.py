'''
DO NOT CHANGE THE NAME OF THIS FILE, or else the tester will not work. 
The first function requires that you replace the given strings with
your personal details. It is important that you enter your student number
and your student email correctly. If your number and email do not match we
will then check your name, so your name acts as a failsafe.
'''

# Student details
from copy import deepcopy



def details():
    student_number = '33191654' #write your student number as a string
    student_email = 'clam0049' + '@student.monash.edu' #write your student email
    name = 'Chi Him Lam' #write your name as it appears on Moodle
    return str(student_number), student_email, name

# Warmup - (0.5 marks)
def is_upper_triangular(a):
    """
    Determines whether (a) is upper triangular.

    For example:
    >>> a = [[2, 1, 1],
    ...      [0, -8, -2],
    ...      [0, 0, 1]]
    >>> is_upper_triangular(a)
    True

    Input : square matrix (a)
    Output: True if all entries of (a) below diagonal are 0;
            False otherwise
    """
    n = len(a)
    col = 1
    for i in range(1,n):
        for element in range(col):
            if not a[i][element] == 0:
                return False
        col = col +1
    return True

    pass


# Task 1 - Part A (0.5 marks)
def is_row_echelon(a):
    """Checks wether a is in echelon (staircase) form.

    >>> a = [[1, 1],
    ...      [0, 1]]
    >>> is_row_echelon(a)
    True

    >>> a = [[1, 0],
    ...      [1, 1]]
    >>> is_row_echelon(a)
    False

    >>> a = [[1, 0],
    ...      [0, 1]]
    >>> is_row_echelon(a)
    True

    >>> a = [[1, 1],
    ...      [0, 0]]
    >>> is_row_echelon(a)
    True

    >>> a = [[0, 0],
    ...      [0, 0]]
    >>> is_row_echelon(a)
    True

    >>> a = [[0, 0],
    ...      [0, 1]]
    >>> is_row_echelon(a)
    False

    >>> a = [[1, 1, 0, 1, 1],
    ...      [0, 0, 1, 0, 1],
    ...      [0, 0, 0, 0, 1],
    ...      [0, 0, 0, 0, 0],
    ...      [0, 0, 0, 0, 0]]
    >>> is_row_echelon(a)
    True
    """
    n = len(a)
    for j in range(n):
        k = pivot_index(a,j)
        if k == None:
            for i in range(j+1, n):
                if a[i][j] != 0:
                    return False
        else:
            for i in range(j+1, k):
                if a[i][j] != 0:
                    return False
    return True
    
    pass


# Task 1 - Part B (0.5 marks)
def pivot_index(a, j, p=None):
    """
    Finds pivot index of matrix a in column j.
    :param a: matrix with n columns
    :param j: column index less or equal n
    :return: row index k greater than j such that a[k][j]!=0 or None if no such index exists
    """
    n = len(a)
    k = p or j
    while k < n and a[k][j] == 0:
        k += 1
    if k < n:
        return k
    
    pass


def echelon(a, b):
    """
    Computes equivalent system in row echelon form of input system
    of linear equations by means of forward elimination. 

    >>> a = [[1, 1, 1],
    ...      [2, 0, 3],
    ...      [3, 1, 4]]
    >>> b = [2, 5, 6]
    >>> echelon(a, b)
    ([[1, 1, 1], [0.0, -2.0, 1.0], [0.0, 0.0, 0.0]], [2, 1.0, -1.0])
    
    >>> a = [[1, 1, 0, 1],
    ...      [-1, -1, 1, 0],
    ...      [-2, -2, -1, 1],
    ...      [-1, -1, -2, 1]]
    >>> b = [1, 0, 0, 0]
    >>> echelon(a, b)
    ([[1, 1, 0, 1], [0.0, 0.0, 1.0, 1.0], [0.0, 0.0, 0.0, 4.0], [0.0, 0.0, 0.0, 0.0]], [1, 1.0, 3.0, 0.0])
    """
    u, c = deepcopy(a), deepcopy(b)
    n = len(u)
    for j in range(n):
        k = pivot_index(u, j, p=None)
        u[j], u[k] = u[k], u[j]
        c[j], c[k] = c[k], c[j]
        for i in range(j+1, len(a)):
            q =u[i][j]/u[j][j]
            u[i] = [u[i][k] - q*u[j][k] for k in range(n)]
            c[i] = c[i] - q*c[j]
    return u, c
    pass


# Task 1 - Part C (0.5 marks)
def solve_by_back_substitution(u, b):
    """
    Solves linear system ux=b for a square matrix u in row echelon
    form or returns None if no solution exists.

    >>> u = [[1, 1, 1],
    ...      [0, -2, 1],
    ...      [0, 0, 0]]
    >>> b = [2, 5, 6]
    >>> solve_by_back_substitution(u, b)

    >>> u = [[1, 1, 1],
    ...      [0, -2, 1],
    ...      [0, 0, 0]]
    >>> b = [2, 1, 0]
    >>> solve_by_back_substitution(u, b)
    [2.5, -0.5, 0.0]

    >>> u = [[1, 1, 0, 1, 1],
    ...      [0, 0, 1, 0, 1],
    ...      [0, 0, 0, 0, 1],
    ...      [0, 0, 0, 0, 0],
    ...      [0, 0, 0, 0, 0]]
    >>> b = [2, 2, 1, 0, 0]
    >>> solve_by_back_substitution(u, b)
    [1.0, 0.0, 1.0, 0.0, 1.0]
    """
    
    pass


# Task 2
# Warmup (0 marks)
def adjacency_matrix(adj_lists):
    """
    >>> lec_graph = [ [2, 4, 5, 6, 7],
    ...               [2, 3, 5, 6 ,7],
    ...               [0, 1, 6, 7],
    ...               [1, 4, 7],
    ...               [0, 3, 6],
    ...               [0, 1],
    ...               [0, 1, 2, 4, 7],
    ...               [0, 1, 2, 4, 7] ]
    >>> adjacency_matrix(lec_graph)
    [[0, 0, 1, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 1, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1], [0, 1, 0, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0, 1, 0], [1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 0, 0, 1], [1, 1, 1, 0, 1, 0, 0, 1]]
    """
    n=len(adj_lists)
    adj_matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(len(adj_lists)):
        for j in adj_lists[i]:
            adj_matrix[i][j]=1
    return adj_matrix
    pass


# Part A: Independent Sets (0.5 marks)
def is_indset(adj_lists, a):
    """
    >>> lec_graph = [ [2, 4, 5, 6, 7],
    ...               [2, 3, 5, 6 ,7],
    ...               [0, 1, 6, 7],
    ...               [1, 4, 7],
    ...               [0, 3, 6],
    ...               [0, 1],
    ...               [0, 1, 2, 4, 7],
    ...               [0, 1, 2, 4, 7] ]
    >>> is_indset(lec_graph, [])
    True
    >>> is_indset(lec_graph, [5])
    True
    >>> is_indset(lec_graph, [0, 2])
    False
    >>> is_indset(lec_graph, [6, 5, 3])
    True
    """
    for w in a:
        for v in a:
            if w in adj_lists[v]:
                return False
    return True
    pass


# Part B - Greedy Maximisation (0.5 marks)
def greedy_indset(adj_lists):
    """
    <Describe the greedy strategy you used here>
    """

    pass


# Task 3 - Extension (OPTIONAL)
def polynomial_fit(points):
    """
    Input: list of co-ordinates (xi, yi) where all xi values are unique. 
    Output: list of the coefficients in order of associated power
    
    >>> points1 = [(1, 4), (-2, 1), (2, 13)]
    >>> polynomial_fit(points1)
    [-1.0, 3.0, 2.0]
	
    >>> points2 = [(-1, -9), (7, 15)]
    >>> polynomial_fit(points2)
    [-6.0, 3.0]
	
    >>> points3 = [(0, 0), (1, 27), (2, 0), (3, -33), (4, 0)]
    >>> polynomial_fit(points3)
    [0.0, 64.0, -40.0, 2.0, 1.0]
    """

    pass



if __name__=='__main__':
    import doctest
    doctest.testmod(verbose=True)
