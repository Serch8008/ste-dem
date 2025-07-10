#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    sum_primary =0 
    sum_secondary =0
    
    for i in range(n):
        sum_primary += arr[i][i]
        sum_secondary += arr[i][n-1-i]
    return abs(sum_primary-sum_secondary)
    

if __name__ == '__main__':
    # Entrada
    n = int(input().strip())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # Cálculo
    result = diagonalDifference(arr)

    # Salida local
    print(result)   
    