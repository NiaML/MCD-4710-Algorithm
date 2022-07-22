#These values can be changed
FIT1045 = True
SHOW_ALL_INFO = False



#############################################################################

#Import statements
from workshop05 import *
import workshop05
from math import ceil
from contextlib import redirect_stdout
import io
from collections.abc import Iterable

def fail_output(s):
    print("{}".format("="*60))
    print(s)
    print("{}".format("="*60))

def communicate(func, input, ans):
    print("checking: {}({})=={}".format(func, input, ans))

def get_function(module, method):
    return getattr(module, method, None)

def get_output(function, func_input, marking):
    try:
        f = io.StringIO()
        with redirect_stdout(f):
            #for when there is more than 1 arg
            if isinstance(func_input, tuple):
                output = function(*func_input)
            else:
                output = function(func_input)
            return (False, output)
    except Exception as e:
        if not marking:
            print(e)
            fail_output(f"...fail (exception thrown)")
        return (True, None)

def process_output(output, ans, options):
    output_function, in_place = options
    if output_function and output:
        return (output_function(output) == output_function(ans))
    if in_place:
        returned_val, modified_var, answer = ans
        return (returned_val == output and modified_var == answer)

def run_cases(module, function, cases, processing, marking=False):
    verbose=SHOW_ALL_INFO
    if marking == True: verbose = False
    # Setup cases count
    cases_failed = 0
    # Run tests
    for case in cases:
        func, input, ans = case
        if verbose: communicate(func, input, ans)
        throws_error, output = get_output(function, input, marking)
        if throws_error:
            cases_failed += 1
            continue
        if output == ans: #or f.getvalue() == ans (used for printing values - no longer used)
            if verbose: print("...passed")
        else:
            if processing and process_output(output, ans, processing):
                if verbose: print("...passed after processing output")
            else:
                if not marking:
                    fail_output(f"...fail (incorrect output)\ngiven output:\t{output} \ncorrect output:\t{case[2]}")
                cases_failed += 1
    return (len(cases)-cases_failed) #num passed tests

def evaluate_module(module, tests, mod_mark=2.5, marking=False):
    if not marking:
        print(f"Evaluating module: {module.__name__}")
    res = 0
    max = 0 #max mark
    t_passed = 0 #percentage of tests passed
    total_tests = 0
    f_passed = 0 #number of functions with 0 errors
    for test in tests:
        cases, mark, *processing = test
        total_tests += len(cases)
        func = cases[0][0]
        if not marking:
            print("{}".format("#"*60))
            print()
            print(f"Testing function {func}:")
        max = max + mark
        # Get function that cases are tested on
        function = get_function(module, func)
        if not function:
            if not marking: print("...fail (function not found)")
            continue
        cases_passed = run_cases(module, function, cases, processing, marking=marking)
        total_cases = len(cases)
        res += round((cases_passed/total_cases)*mark, 4) #scale res by number of marks the function is worth
        t_passed += cases_passed
        if cases_passed==total_cases: f_passed += 1
        if not marking:
            if cases_passed==total_cases:
                print("All cases passed")
            else:
                print("Some cases failed")
            print()
    if not marking:
        print("{}".format("#"*60))
        print()

    #Scale and print Results
    scaled = 0

    if res/max>=0.95 and f_passed > 1: scaled = 2.5
    elif res/max>=0.7 and f_passed > 1: scaled = 2
    elif res/max>=0.5 and f_passed > 1: scaled = 1.5
    elif f_passed >= 1: scaled = 1
    elif res/max>0: scaled = 0.5
    if not marking:
        print(f"Percentage of tests passed: {round(t_passed/total_tests*100,2)}%")
        print(f"Scaled percentage of tests passed: {round(res/max*100,2)}%")
        print(f"Total correct functions: {f_passed}/{len(tests)}")
        print()
        print(f"Total marks: {scaled}/{mod_mark}")
    return scaled

#############################################################################

#Task 1
WORD = \
  [('word_from_file', 'files/task1A.txt', 'Once'),
   ('word_from_file', 'files/test1.txt', 'cat'),
   ('word_from_file', 'files/test2.txt', 'In'),
   ('word_from_file', 'files/test3.txt', "'Dogs'")]

TABLE = \
  [('nested_int_list_from_file', 'files/task1B.txt', [[2,1,3],[3,1,3],[2,9]]),
   ('nested_int_list_from_file', 'files/test4.txt', []),
   ('nested_int_list_from_file', 'files/test5.txt', [[1,0],[0,1]]),
   ('nested_int_list_from_file', 'files/test6.txt', [[1]])]

#Task 2
empty_graph = [[0,0,0,0],
               [0,0,0,0],
               [0,0,0,0],
               [0,0,0,0]]

simple_graph = [[0,1,1,1],
               [1,0,1,0],
               [1,1,0,0],
               [1,0,0,0]]

directed_graph = [[0,1,0,0,0],
                  [1,0,0,1,0],
                  [0,0,0,0,0],
                  [0,0,0,0,1],
                  [1,0,1,0,0]] #from Tutorial 3, Practice, Graph H

DEGREE = \
  [('degree', (empty_graph, 0), 0),
   ('degree', (simple_graph, 1), 2),
   ('degree', (directed_graph, 2), 0),
   ('degree', (directed_graph, 1), 2),]

IS_PATH = \
  [('is_path', (empty_graph, [0,1]), False),
   ('is_path', (simple_graph, [0,1,2]), True),
   ('is_path', (directed_graph, [1,3,4]), True),
   ('is_path', (directed_graph, [0,4,2]), False)]

#Task 3 new

grid_1_1 = [[0]]
grid_3_3 = [[0, 1, 0, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 1, 0, 1, 0]]
grid_2_8 = [[0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0]]
grid_6_3 = [[0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]]

GRID = \
    [('grid_graph', (1, 1), grid_1_1),
     ('grid_graph', (3, 3), grid_3_3),
     ('grid_graph', (2, 8), grid_2_8),
     ('grid_graph', (6, 3), grid_6_3)]


#Task 4
table1 = [[1,2], [2,1]] #1
table1A = [[2,1], [1,2]]
table2 = [[3,2,3],[2,2,3],[4,2,3],[1,2,3]] #0
table2A = [[1,2,3],[2,2,3],[3,2,3],[4,2,3]]
table3 = [[3,2,3],[2,1,3],[4,2,3],[1,1,3]] #1
table3A = [[2,1,3],[1,1,3],[3,2,3],[4,2,3]]
table4 = [[2,3],[1,1],[2,2],[1,2],[2,1],[1,3]] #0
table4A = [[1,1],[1,2],[1,3],[2,3],[2,2],[2,1]]

SORT_TABLE = \
  [('sort_table', (table1, 1), (None, table1, table1A)),
   ('sort_table', (table2, 0), (None, table2, table2A)),
   ('sort_table', (table3, 1), (None, table3, table3A)),
   ('sort_table', (table4, 0), (None, table4, table4A))]


evaluate = \
  [(WORD, 0.5),
   (TABLE, 0.5),
   (DEGREE, 0.5),
   (IS_PATH, 0.5),
   (GRID, 1),
   (SORT_TABLE, 1, None, True)] 

#evaluate += [] if FIT1045 else [(task5, 2, output_process)] #weight is 2 for adv
################################################################################

def main():
    if details() == ('', '@student.monash.edu', ''):
        print("Tester will not run if details are not completed.")
        return
    evaluate_module(workshop05, evaluate, marking=False)


def mark():            
    num,email,name = details()
    score = evaluate_module(workshop05, evaluate, marking=True)
    print(','.join([num,email,name,str(score)]))

if __name__ == "__main__":
    main()
