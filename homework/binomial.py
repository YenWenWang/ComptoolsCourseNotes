#!/usr/bin/env python
"""module for binomial coefficients"""

import argparse
import math
# use an Argument Parser object to handle script arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, help = "total number of items to choose from")
parser.add_argument("-k", type=int, help = "number of items to choose")
parser.add_argument("-l", "--log", action="store_true", help = "returns the log binomial coefficient")
parser.add_argument("-test", action="store_true", help="tests the module and quits")
args = parser.parse_args()

# test argument problems early:
if not args.test and __name__ == '__main__':
    if args.n<0:
        raise Exception("argument -n must be 0 or positive")
    if args.k>args.n:
        raise Exception("argument -k must be less or equals to argument -n")
    # no error if file imported as module

def choose(n=args.n,k=args.k):
    """returns the binomial coefficient.
    Examples:
    >>> choose(5,3)
    10
    """
    if k > n or n < 0:
        print("n must be 0 or positive\nk must be less or equals to")
        return
    
    s=0
    for i in range(k,n):
        s=s+math.log(i+1)
    
    for i in range(0,n-k):
        s=s-math.log(i+1)
    
    if args.log:
        return s
    else:
        return int(math.exp(s))

def runTests():
    print("testing the module...")
    if args.n:
        print("ignoring n for testing purposes")
    import doctest
    doctest.testmod()
    print("done with tests.")

if __name__ == '__main__':
    if args.test:
        runTests()
    else:
        print(choose())
