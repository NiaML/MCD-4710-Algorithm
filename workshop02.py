from random import random

from numpy import true_divide
'''
DO NOT CHANGE THE NAME OF THIS FILE, or else the tester will not work. 
The first function requires that you replace the given strings with
your personal details. It is important that you enter your student number
and your student email correctly. If your number and email do not match we
will then check your name, so your name acts as a failsafe.
'''
# Student details
def details():
    student_number = '33191654 ' #write your student number as a string
    student_email = 'clam0049' + '@student.monash.edu' #write your student email
    name = 'Chi Him Lam' #write your name as it appears on Moodle
    return str(student_number), student_email, name

###Task 1
def calculate(x,y,operator):
    """
    >>> calculate(3, 5, '+')
    8
    >>> calculate(3, 5, '-')
    -2
    >>> calculate(3, 5, 'x')
    15
    >>> calculate(3, 5, '/')
    0.6
    """    
    if operator == '+':
        return (x + y)
    if operator == '-':
        return (x - y)
    if operator == 'x':
        return (x * y)
    if operator == '/':
        return x/y
    pass


###Task 2
def is_leap_year(year):
    """
    >>> is_leap_year(1)
    False
    >>> is_leap_year(100)
    False
    >>> is_leap_year(2000)
    True
    >>> is_leap_year(2019)
    False
    >>> is_leap_year(2040)
    True
    >>> is_leap_year(2100)
    False
    """
    
    if year % 4 == 0:
        if year%100==0:
            if year %400==0:
                return True
            return False
        return True
    elif year%4 !=0 or year<0:
        return False
    #return year%4==0 and (year%100!=0 or year%400==0)
    pass

def leap_year_answer(year):
    """
    >>> leap_year_answer(1)
    'Year 1 was not a leap year'
    >>> leap_year_answer(100)
    'Year 100 was not a leap year'
    >>> leap_year_answer(2000)
    'Year 2000 was a leap year'
    >>> leap_year_answer(2019)
    'Year 2019 was not a leap year'
    >>> leap_year_answer(2040)
    'Year 2040 will be a leap year'
    >>> leap_year_answer(2100)
    'Year 2100 will not be a leap year'
    """
    import datetime
    
    if is_leap_year(year):
        if year<datetime.datetime.now().year:
            return 'Year ' +str(year)+ ' was a leap year'
        if year>=datetime.datetime.now().year:
            return 'Year ' +str(year)+ ' will be a leap year'
    elif not is_leap_year(year):
        if year<datetime.datetime.now().year:
            return 'Year ' +str(year)+ ' was not a leap year'
        if year>=datetime.datetime.now().year:
            return 'Year ' +str(year)+ ' will not be a leap year'
    pass

###Task 3
def next_triangular_number(num):
    """
    >>> next_triangular_number(5)
    6
    >>> next_triangular_number(25)
    28
    >>> next_triangular_number(40)
    45
    >>> next_triangular_number(2000)
    2016
    """
    trig_num = 0
    for i in range(num):
        while trig_num<num:
            trig_num += i
    return trig_num
    pass

###Task 4
def add(numbers):
    """
    >>> add([])
    0
    >>> add([25])
    0
    >>> add([92, 61, 97, 10, -39])
    71
    >>> add([-24, -25, -33, 32, -81, -58, 28, -4, -30, -69, 44, -41])
    -165
    """

    pass

def flip(binary_string):
    """
    >>> flip('')
    ''
    >>> flip('01')
    '10'
    >>> flip('101')
    '010'
    >>> flip('001011111111')
    '110100000000'
    """
    flipped = ''
    for i in range(len(binary_string)):
        if binary_string[i] == '0':
            flipped += '1'
        elif binary_string[i] == '1':
            flipped += '0'
    return flipped
    pass

###Task 5 - Extension (OPTIONAL)
def n_even_fibonacci(n):
    """
    >>> n_even_fibonacci(0)
    []
    >>> n_even_fibonacci(5)
    [0, 2, 8, 34, 144]
    >>> n_even_fibonacci(10)
    [0, 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418]
    >>> n_even_fibonacci(12)
    [0, 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578]
    """
    pass


###Challenge - OPTIONAL
from math import e
def estimate_e(error):
    """
    <WRITE YOUR ANALYSIS HERE>
    >>> estimate_e(1)
    2.0
    >>> estimate_e(0.1)
    2.6666666666666665
    >>> estimate_e(0.01)
    2.708333333333333
    >>> estimate_e(0.005)
    2.7166666666666663
    >>> estimate_e(0.001)
    2.7180555555555554
    >>> estimate_e(0.0000000001)
    2.7182818284467594
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
