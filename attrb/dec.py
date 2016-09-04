import time

# random argument decorato
# func = timeit(func)
# func == wrapper
# func(arg) == wrapper(arg)
def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        cost = time.time() - start
        print "run this function used ", cost
        return ret 

    return wrapper
    
# decorator with argument
def whilt_list_filter(hosts):
    def decor(func):
        def wrapper(*args, **kwargs):
            ip = kwargs['ip']
            if ip in hosts:
                return func(*args, **kwargs)
            else:
                raise Exception('forbbindeen')
        return wrapper
    return decor
            

if __name__ == '__main__':

    @timeit
    def func_a(a):
        return a**a

    func_a(100)
    print func_a(a=80)

    @whilt_list_filter(hosts=[1,2,3])
    def func_b(ip):
        print ip

    func_b(ip=1)
    func_b(ip=2)
    func_b(ip=5)
