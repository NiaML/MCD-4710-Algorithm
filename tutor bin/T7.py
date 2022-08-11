lst = [-9, -3, 5, 19, -1, 3, 11, 17]

def x( a , b ):
    ret_val = []
    n1 = len ( a)
    n2 = len ( b)
    i = 0
    j = 0
    while i < n1 and j < n2 :
        if a[ i] > b[ j ]:
            ret_val . append ( b[ j ])
            j = j + 1
        else :
            ret_val . append ( a[ i ])
            i = i + 1
    print(a[ i ::],b[ j ::])
    return ret_val + a[ i ::] + b[ j ::]

def x_no( a , b ):
    ret_val = []
    n1 = len ( a)
    n2 = len ( b)
    i = 0
    j = 0
    while i < n1 and j < n2 :
        if a[ i] > b[ j ]:
            ret_val . append ( b[ j ])
            j = j + 1
        else :
            ret_val . append ( a[ i ])
            i = i + 1
    print(a[ i ::],b[ j ::])
    return ret_val 


a = lst[:len(lst)//2]
b = lst[len(lst)//2::]

pass