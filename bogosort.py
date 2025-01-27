# -*- coding: utf-8 -*-
"""BogoSort.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DhtXZBfpkFgLlDdZDJH5F3mvSrZhg87Q
"""

import random

#sort an array a(0, ..., n-1)
def bogoSort(a):
    n = len(a)
    while not is_sorted(a):
        shuffle(a)
        print("Current array values", a)

def is_sorted(a):
  n = len(a)
  for i in range(0,n-1):
    if a[i] > a[i+1]:
        return False
    return True


#Python generates a random integer between 0 and n-1
def shuffle(a):
    n = len(a)
    for i in range(0,n):
        r = random.randint(0,n-1)
        a[i], a[r] = a[r], a[i]

#sorting the array
a = [3,2,4,5,6]
bogoSort(a)
print("Sorted array")
print("".join(str(x) for x in a))