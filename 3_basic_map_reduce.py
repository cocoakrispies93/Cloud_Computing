import time
from functools import reduce

# Return the max lenght touple from p and c
def reducer(p, c):    
    if p[1] > c[1]:
        return p
    return c

if __name__ == '__main__':
    list_of_strings = ['abc', 'python', 'dima'] 
    large_list_of_strings = list_of_strings*100000000   
    
    start = time.process_time()
    mapper = len
    
    # Step 1: Apply len function in to all large_list_of_strings and returns map object
    mapped = map(mapper, large_list_of_strings)

    # join values in two data structures and create a touple
    mapped = zip(large_list_of_strings, mapped)
    
    # Step 2: Apply reducer function to a1, a2 -> r1, r1, a3 -> r2, r2, a4 -> r4
    # This step can be implemented with normal for loop

    reduced = reduce(reducer, mapped)
    print(reduced)
    print(time.process_time() - start)
    