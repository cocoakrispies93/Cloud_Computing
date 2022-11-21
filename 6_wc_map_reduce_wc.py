import time
from functools import reduce

# Return the max lenght touple from p and c
def reducer(p, c):
    for k in c.keys():
        if k in p:
            p[k] = p[k]+1
        else:
            p[k] = 1
    return p


def word_count(s):
    return {s: 1}


if __name__ == '__main__':
    list_of_strings = ['abc', 'python', 'dima'] 
    large_list_of_strings = list_of_strings*10000000
    
    start = time.process_time()
    mapper = word_count
    
    # Step 1: Apply len function in to all large_list_of_strings and returns map object
    mapped = map(mapper, large_list_of_strings)
   

    # Step 2: Apply reducer function to a1, a2 -> r1, r1, a3 -> r2, r2, a4 -> r4
    # This step can be implemented with normal for loop

    reduced = reduce(reducer, mapped)
    
    print(reduced)
    print(time.process_time() - start)
    