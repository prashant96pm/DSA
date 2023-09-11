from os import *
from sys import *
from collections import *
from math import *

''' Number Star pattern 1
 Sample Output :
 5432*
 543*1
 54*21
 5*321
 *4321'''


n = int(input())

for i in range(n):
    for j in range(n):
        if j == n-i-1:
            print('*', end='')
        else:
            print(n-j, end='')
    print()
