import time

def timeit(func):
    ''' show time function cost'''
    def wrapper(*args):
        start = time.time()
        ret = func(*args)
        cost = time.time() - start
        print "run this function used ", cost
        return ret 
    return wrapper
