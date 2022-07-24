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


# Task 1
def word_from_file(file):
    
    f = open(file, 'r')
    words = f.read().split() #  read the whole file and split the words as strings
    f.close()
    return words[0] # return the first word
    pass

def nested_int_list_from_file(file):
    ans = []
    # safy guard if the file does not exist
    import os
    # get current path
    path = os.path.join(os.getcwd()+'\\'+file)
    if not os.path.exists(path):
        return ans
    f = open(file, 'r')
    
    #appending elements
    for line in f:
        print(line)
        line    = line.strip().split(',') # split the words
        ans.append(line)            # append the words as strings
    f.close()

    for row in range(len(ans)):
        for col in range(len(ans[row])):
            # convert string to int
            ans[row][col]   =   int(ans[row][col])
    return ans
    pass

# Task 2
def degree(graph, vertex):
    degree = 0
    for i in range(len(graph[vertex])):
        if graph[vertex][i] == 1:
            degree += 1

    return degree
    pass

def is_path(graph, path):
    ans = True # set ans as boolean type
    
    for i in range(len(path)-1):
        if not graph[path[i]][path[i+1]]:
            ans = False
            return ans
    return ans
    pass

# Task 3
def print_as_grid(graph, n):
    """
    Input : Grid graph (graph), number of columns (n)
    Effect: Prints the graph organised as grid
    """
    
    def index(r, c):
        return r*n + c
    
    m = len(graph) // n
    
    for i in range(m):
        for j in range(n):
            print('*', end='')
            k = index(i, j)
            if j < n-1 and graph[k][index(i, j+1)]:
                print('---', end='')
            else:
                print('   ', end='')
        print('\n', end='')
        if i < m - 1:
            for j in range(n):
                k = index(i, j)
                if graph[k][index(i + 1, j)]:
                    print('|', end='')
                else:
                    print(' ', end='')
                if j < n-1:
                    print('   ', end='')
            print('\n', end='')


def grid_graph(m, n):
    pass


# Task 4
def sort_table(table, col):
    pass
