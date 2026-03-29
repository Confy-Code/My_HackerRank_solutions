#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    
    if len(arr) == 1:
        return "YES"
    
    mid = len(arr) // 2
    
    left_sum = sum(arr[:mid])
    right_sum = sum(arr[mid + 1:])
    counts = 0
    
    while 0 <= mid < len(arr) - 1 and counts < len(arr):
        if left_sum < right_sum:
            left_sum += arr[mid]
            mid += 1
            right_sum -= arr[mid]
            
        elif left_sum > right_sum:
            right_sum += arr[mid]
            mid -= 1
            left_sum -= arr[mid]
            
        else:
            return "YES"
        
        counts += 1
        
    return "NO"
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
