# -*- coding: utf-8 -*-
"""selectionSort.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BSMi9KRjmdLa-9mLaowbSM-t4eXh_rk_
"""

def selectionSort(arr):
  n = len(arr)
  # Traverse through all array elements
  for i in range(n):
      # Find the minimum element in remaining unsorted array
      min_idx = i
      for j in range(i+1, n):
          if arr[j] < arr[min_idx]:
              min_idx = j

      # Swap the found minimum element with the first element of the unsorted part
      arr[i], arr[min_idx] = arr[min_idx], arr[i]

      #Print the array after each iteration of selection sort
      print("After iteration", i+1, ":", arr)

  return arr

# Driver code to test above:
arr = [64, 25, 12, 22, 11]
print("Original array:", arr)
sorted_arr = selectionSort(arr)
print("Sorted array:", sorted_arr)