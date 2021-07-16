# Analysis of Algorithms  - CS323 Queens College
# Assignmnent 1: Quick Sort Evaluation
# Python3 implementation of QuickSort 
# Michael Meneses
# Sources Used:
# https://www.geeksforgeeks.org/quick-sort/

#  We are evaluating the runtime of the following
# 1. Randomized pivot 

# 2. Fixed Pivot

# 3. Switiching to Insertion sort when high - low < threshold

# To test the code we need to measure
# clock time
# number of comparisons performed

 
# This Function handles sorting part of quick sort
# start and end points to first and last element of
# an array respectively
def partition(start, end, array):
     
    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]
     
    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:
         
        # Increment the start pointer till it finds an
        # element greater than  pivot
        while start < len(array) and array[start] <= pivot:
            start += 1
             
        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[end] > pivot:
            end -= 1
         
        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if(start < end):
            array[start], array[end] = array[end], array[start]
     
    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]
    
    # Returning end pointer to divide the array into 2
    return end
     
# The main function that implements QuickSort
def quick_sort(start, end, array):
     
    if (start < end):
         
        # p is partitioning index, array[p]
        # is at right place
        p = partition(start, end, array)
         
        # Sort elements before partition
        # and after partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)
         
# Driver code

#Import numpy for test data
import numpy as np

arr1 = np.random.randint(0,100,100) #Random Array of 100 elements
arr2 = np.random.randint(0,1000,1000) #Random Array of 1,000 elements
arr3 = np.random.randint(0,10000,10000) #Random Array of 10,000 elements

#Import clock to measure time
import time
time = time.clock()

print(f'Unsorted array: {arr1}')

quick_sort(0, len(arr1) - 1, arr1)
 
print(f'Sorted array: {arr1}')
     
