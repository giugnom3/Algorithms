# -*- coding: utf-8 -*-
"""BruteForce.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1COtK2t07XBJcQwM0CqXb9JxNDi4l-5w1
"""

def brute_force_max(arr):
  max_value = arr[0]
  for num in arr:
    if num > max_value:
      max_value = num
  return max_value

