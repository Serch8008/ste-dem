#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

# def compareTriplets(a, b):
    # Write your code here
    # alice=0
    # bob=0
    
    # for x,y in zip(a,b):
    #     if x>y:
    #         alice+=1
    #     elif x<y:
    #         bob+=1
    # return [alice, bob]
    
def compareTriplets(a, b):
    alice = sum(1 for x, y in zip(a, b) if x > y)
    bob = sum(1 for x, y in zip(a, b) if x < y)
    return [alice, bob]    


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    print(' '.join(map(str, result)))