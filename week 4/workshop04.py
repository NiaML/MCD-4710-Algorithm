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

# Simple Functions
def is_in(char, string):
    i=0
    while i < len(string):
        if char == string[i]:
            return True
        i+=1
    return False
    # another method:
    # if string.count(char)>0 :
    #     return True
    # else :
    #     return False

def is_sorted(seq):
    i=0
    while i < len(seq)-1:
        if seq[i] > seq[i+1]:
            return False
        i+=1
    return True

def abs(x):
    if x<0:
        return -x
    else:
        return x

def all(lst):
    i=0
    while i < len(lst):
        if bool(lst[i]) == False:
            return False
        i+=1
    return True

def any(lst):
    i=0
    while i < len(lst):
        if bool(lst[i]):
            return True
        i+=1
    return False

def max(lst):
    i=0
    ans=lst[0]
    while i < len(lst):
        if ans < lst[i]:
            ans=lst[i]
        i+=1
    return ans

def min(lst):
    i=0
    ans=lst[0]
    while i < len(lst):
        if ans > lst[i]:
            ans=lst[i]
        i+=1
    return ans

def reversed(lst):
    i=len(lst)-1
    ans=[]
    while i >= 0:
        ans.append(lst[i])
        i-=1

    return ans

def sum(lst):
    i=0
    ans=0
    while i < len(lst):
        ans+=lst[i]
        i+=1
    return ans


# complex functions
def bin(x):
    if x>=0:
        prefix='0b'
    else:
        prefix='-0b'
    x=abs(x)
    binString=''
    if x==0:
        return prefix+'0'
    while x>0:
        binString+=str(x%2)
        x//=2
        
    return prefix + binString[::-1]

def enumerate(seq, start=0):
    i=start
    ans=[]
    index_temp=0
    while index_temp < len(seq):
        ans.append((i,seq[index_temp]))
        i+=1
        index_temp+=1
    
    return ans

def filter(function, seq):
    ans=[]
    for i in seq:
        if function(i):
            ans.append(i)
    return ans

def map(function, seq):
    ans=[]
    for i in seq:
        ans.append(function(i))
    return function

def lim_range(start, stop, step=1):
    ans=[]
    step=abs(step)
    i=start
    if start==stop:
        return []
    elif start<stop:
        while i < stop:
            ans.append(i)
            i+=step
    else:
        while i > stop:
            ans.append(i)
            i-=step
    return ans

def round(number, ndigits=0):
    ndigits=abs(ndigits)

    

def set(lst):
    ans=[]
    for i in lst:
        if i not in ans:
            ans.append(i)
    return ans


