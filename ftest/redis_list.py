# coding:utf-8
'''
  test redis list operation speed
'''
import random
import redis
import time
import cPickle as pickle


cache = redis.StrictRedis()
HASH_KEY = 'hash_oids'
LIST_KEY = 'list_oids'


def genrate_oids(length):
    '''
    generate oids which length is 15.
    simulate taobao order id
    '''
    l = range(10)*2
    oids = []
    for i in xrange(length):
        oid = random.sample(l, 15)
        oid = [ str(i) for i in oid ]
        oids.append(''.join(oid))
    return oids

def init():
    oids = genrate_oids(5000)
    cache.set(HASH_KEY, pickle.dumps(oids))
    cache.lpush(LIST_KEY, *oids)
    return oids

def hash_judge_in(oid):
    oids = cache.get(HASH_KEY)
    oids = pickle.loads(oids)
    if oid in oids:
        return 1
    return 0

def hash_loop(oids):
    count = 0
    for oid in oids:
        i = hash_judge_in(oid)
        count += i
    print "hash test mached %d finally"%count

def list_judge_in(oid):
    len_ = cache.llen(LIST_KEY)
    oids = cache.lrange(LIST_KEY, 0, len_)
    if oid in oids:
        return 1
    return 0

def list_loop(oids):
    count = 0
    for oid in oids:
        i = list_judge_in(oid)
        count += i
    print "list test mached %d finally"%count

if __name__ =="__main__":
    test_oids = init()
    test_oids = test_oids[:2000]

    start = time.time()
    hash_loop(test_oids)
    print "hash cost %s seconds"%(time.time() - start)

    start = time.time()
    list_loop(test_oids)
    print "list cost %s seconds"%(time.time() - start)
