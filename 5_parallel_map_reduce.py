import time
from functools import reduce
from multiprocessing import Pool

def reducer(p, c):
    if p[1] > c[1]:
        return p
    return c

def chunkify(seq, number_of_chunks):
    return (seq[i::number_of_chunks] for i in range(number_of_chunks))

mapper = len

def chunks_mapper(chunk):
    mapped_chunk = map(mapper, chunk) 
    mapped_chunk = zip(chunk, mapped_chunk)
    return reduce(reducer, mapped_chunk)

if __name__ == '__main__':
    list_of_strings = ['abc', 'python', 'dima'] 
    large_list_of_strings = list_of_strings*100000000   
    
    start = time.process_time()
    data_chunks = chunkify(large_list_of_strings, number_of_chunks=8)

    pool = Pool(8)

    #step 1:
    mapped = pool.map(chunks_mapper, data_chunks)
    
    #step 2:
    reduced = reduce(reducer, mapped)
    print(reduced)
    print(time.process_time() - start)
    