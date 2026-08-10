#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here

    diff_arr = [0] * (n + 1)
    
    for start, end, k in queries:
        diff_arr[start - 1] += k 
        diff_arr[end] -= k
        
    prefix_sum = [0] * len(diff_arr)
    prefix_sum[0] = diff_arr[0]
    
    for idx in range(1, len(diff_arr)):
        prefix_sum[idx] = prefix_sum[idx -1] + diff_arr[idx]
        
    return max(prefix_sum)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
