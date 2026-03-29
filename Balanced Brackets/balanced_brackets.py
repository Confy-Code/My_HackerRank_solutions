#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    
    if s == "":
        return "NO"
    
    dictionary = {'{': '}',
                    '(': ')',
                    "[": "]"}
    stack = []
    
    for bracket in s:
        if bracket in dictionary:
            stack.append(bracket)
            
        else:
            if not stack:
                return "NO"
            if stack:
                if dictionary[stack.pop()] != bracket:
                    return "NO"
                
    return "YES" if len(stack) == 0 else "NO"
                    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
