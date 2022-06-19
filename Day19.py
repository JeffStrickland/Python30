"""
Day 19 - Generators

Given an integer k, print the first k non-prime positive integers,
each on a new line. For example, if k = 10, the output would be:
1 4 6 8 9 10 12 14 15 16 18 20
Test 1:
- Inputs
    12
- Outpus
    1 4 6 8 9 10 12 14 15 16 18 20
"""

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    
    # The running integer that's checked for primeness
    q = 2
    
    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1

def gen_call(x):
    count = 0
    for i in gen_primes():
        if count < x:
            print(i)
            count += 1
        else:
            break
        
    
#print(gen_call(10))

def not_prime_gen():
    x = 0
    if x % 2 == 0:
        yield x
        x += 1
    else:
        x += 1
            
def gen_call_not_prime(z):
    count = 0
    for i in not_prime_gen():
        if count < z:
            print(i)
            count += 1
        else:
            break
    
print(gen_call_not_prime(10))
