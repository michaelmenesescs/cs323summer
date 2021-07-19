# Analysis of Algorithms  - CS323 Queens College
# Assignmnent 1: Quick Sort Evaluation
# Python3 implementation of QuickSort 
# Michael Meneses
# Jonathan Bernard
# Jacob Brown
# Sources Used:
# https://www.geeksforgeeks.org/quick-sort/

#  We are evaluating the runtime of the following
# 1. Randomized pivot 
# 2. Fixed Pivot
# 3. Switiching to Insertion sort when high - low < threshold
# To test the code we need to measure
# clock time
# number of comparisons performed

#dependencies
import time
time1 =  time.time()
import numpy as numpy
import random
from tabulate import tabulate
import pandas as pd
ncomp = 0

# This Function handles sorting part of quick sort
# start and end points to first and last element of
# an array respectively
def partition(start, end, array, spot):
    if(spot == 'high'):
        # Initializing pivot's index to start    
        i = (start - 1)
        pivot_index = end
        pivot = array[pivot_index]
        for j in range(start, end):  
            # If current element is smaller than or
            # equal to pivot
            if array[j] <= pivot:
                #comparison
                global ncomp
                ncomp += 1
    
                # increment index of smaller element
                i = i+1
                array[i], array[j] = array[j], array[i]    
        array[i+1], array[end] = array[end], array[i+1]
        return (i+1)
    elif(spot == 'low'):
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
                ncomp += 2 

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
    else:
        # Generating a random number between the
        # starting index of the array and the
        # ending index of the array.
        randpivot = random.randrange(start, end)
    
        # Swapping the starting element of
        # the array and the pivot
        array[start], array[randpivot] = array[randpivot], array[start]
        #return partition(array, start, end, 'low')

        piv = start # pivot
     
        # a variable to memorize where the
        i = start + 1
        
        # partition in the array starts from.
        for j in range(start + 1, end + 1):
            
            # if the current element is smaller
            # or equal to pivot, shift it to the
            # left side of the partition.
            if array[j] <= array[piv]:
                ncomp += 1
                array[i] , array[j] = array[j] , array[i]
                i = i + 1
        array[piv] , array[i - 1] = array[i - 1] , array[piv]
        piv = i - 1
        return (piv)   
     
# The main function that implements QuickSort
def quick_sort(start, end, array, spot, threshold):

    if(end-start < threshold):
        insertionSort(array, start, end)

    if (start < end):
        global ncomp
        ncomp += 1
        
        # p is partitioning index, array[p]
        # is at right place
        p = partition(start, end, array, spot) 
        # Sort elements before partition
        # and after partition
        quick_sort(start, p - 1, array, spot, threshold)
        quick_sort(p + 1, end, array, spot, threshold)

def insertionSort(arr, start, end):
 
    # Traverse through 1 to len(arr)
    for i in range(start + 1, end + 1):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= start and key < arr[j] :
                global ncomp
                ncomp += 1
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

# Driver code
pivot_spot = 'low' #low, high, rand
threshold = 10        
arr1 = numpy.random.randint(0,100,100)
arr2 = numpy.random.randint(0,1000,1000)
arr3 = numpy.random.randint(0,10000,10000)
set1 = []
set2 = []
set3 = []

#Trials

#Set 1, n=100, pivot=start
print("--------------------------------")
print("Data Set #1: N = 100, Fixed Pivot (Low)")
print("--------------------------------")
time1 = time.time() 
#print(f'Unsorted array: {arr1}')
quick_sort(0, len(arr1) - 1, arr1, pivot_spot, -1)
#print(ncomp)
time2 = time.time()
#print(f'Sorted array: {arr1}')
rtime = time2-time1
print(f'Runtime: {rtime}')
#set1.append({'n': 100, 'pivot': pivot_spot, 'time': rtime, 'comp': ncomp})
#print(set1)
print(f'Total comparisons: {ncomp}')
print("--------------------------------")




#Set 1, n=100, pivot=end
ncomp = 0
print("--------------------------------")
print("Data Set #1: N = 100, Fixed Pivot (High)")
print("--------------------------------")
pivot_spot = 'high'
time1 = time.time()
quick_sort(0, len(arr1) - 1, arr1, pivot_spot, -1)
time2 = time.time()
#print(f'Sorted array: {arr1}')
print(f'Runtime: {time2-time1}')
#set1.append({'n': 100, 'pivot': pivot_spot, 'time': time2-time1, 'comp': ncomp})
print(f'Total comparisons: {ncomp}')
print("--------------------------------")

#Set 1, n=100, pivot=random
ncomp = 0
print("--------------------------------")
print("Data Set #1: N = 100, Random Pivot")
print("--------------------------------")
pivot_spot = 'rand'
time1 = time.time()
quick_sort(0, len(arr1) - 1, arr1, pivot_spot, -1)
time2 = time.time()
#print(f'Sorted array: {arr1}')
print(f'Runtime: {time2-time1}')
print(f'Total comparisons: {ncomp}')
print("--------------------------------")
set1.append({'n': 100, 'pivot': pivot_spot, 'time': time2-time1, 'comp': ncomp})


#Set 1(insertion sort hybrid): n=100, pivot=random, threshold=10
print("--------------------------------")
print("Data Set #1: N = 100, Insertion sort")
print("--------------------------------")
ncomp = 0
arr1 = numpy.random.randint(0,100,100)
pivot_spot = 'rand'
time1 = time.time()
quick_sort(0, len(arr1) - 1, arr1, pivot_spot, threshold)
time2 = time.time() 
#print(f'Sorted array: {arr1}')
print(f'Runtime: {time2-time1}')
set1.append({'n': 100, 'pivot': pivot_spot, 'time': time2-time1, 'comp': ncomp})
print(f'Total comparisons: {ncomp}')
print("--------------------------------")




#Set 2, n=1000, pivot=start
print("--------------------------------")
print("Data Set #2: N = 1000, Fixed Pivot (Low)")
print("--------------------------------")
ncomp = 0
pivot_spot = 'low'
time1 = time.time()
quick_sort(0, len(arr2) - 1, arr2, pivot_spot, -1)
time2 = time.time()
#print(f'Sorted array: {arr2}')
print(f'Runtime: {time2-time1}')
set2.append({'n': 1000, 'pivot': pivot_spot, 'time': time2-time1, 'comp': ncomp})
print(f'Total comparisons: {ncomp}')
print("--------------------------------")

#Set 2, n=1000, pivot=end
print("--------------------------------")
print("Data Set #2: N = 1000, Fixed Pivot (High)")
print("--------------------------------")
ncomp = 0
arr2 = numpy.random.randint(0,1000,1000)
pivot_spot = 'high'
time1 = time.time()
quick_sort(0, len(arr2) - 1, arr2, pivot_spot, -1)
time2 = time.time()
#print(f'Sorted array: {arr2}')
print(f'Runtime: {time2-time1}')
set2.append({'n': 1000, 'pivot': pivot_spot, 'time': time2-time1, 'comp': ncomp})
print(f'Total comparisons: {ncomp}')
print("--------------------------------")

#Set 2, n=1000, pivot=random
print("--------------------------------")
print("Data Set #2: N = 1000, Random")
print("--------------------------------")
ncomp = 0
arr2 = numpy.random.randint(0,1000,1000)
pivot_spot = 'rand'
time1 = time.time()
quick_sort(0, len(arr2) - 1, arr2, pivot_spot, -1)
time2 = time.time()
#print(f'Sorted array: {arr2}')
print(f'Runtime: {time2-time1}')
set2.append({'n': 1000, 'pivot': pivot_spot, 'time': time2-time1, 'comp': ncomp})
print(f'Total comparisons: {ncomp}')
print("--------------------------------")

#Set 2(insertion sort hybrid): n=1000, pivot=random, threshold=10
print("--------------------------------")
print("Data Set #2: N = 1000, Insertion Sort")
print("--------------------------------")
ncomp = 0
arr2 = numpy.random.randint(0,1000,1000)
pivot_spot = 'rand'
time1 = time.time()
quick_sort(0, len(arr2) - 1, arr2, pivot_spot, threshold)
time2 = time.time()
#print(f'Sorted array: {arr2}')
print(f'Runtime: {time2-time1}')
#set2.append({'n': 1000, 'pivot': pivot_spot, 'time': time2-time1, 'comp': ncomp})
print(f'Total comparisons: {ncomp}')
print("--------------------------------")

#Set 3,  n=10000, pivot=start
print("--------------------------------")
print("Data Set #3: N = 1000, Fixed Pivot (Low)")
print("--------------------------------")
ncomp = 0
pivot_spot = 'low'
time1 = time.time()
quick_sort(0, len(arr3) - 1, arr3, pivot_spot, -1)
time2 = time.time()
#print(f'Sorted array: {arr3}')
print(f'Runtime: {time2-time1}')
set3.append({'n': 10000, 'pivot': pivot_spot, 'time': time2-time1, 'comp': ncomp})
print(f'Total comparisons: {ncomp}')
print("--------------------------------")


#Set 3, n=10000, pivot=end
print("--------------------------------")
print("Data Set #3: N = 1000, Fixed Pivot (High)")
print("--------------------------------")
ncomp = 0
arr3 = numpy.random.randint(0,10000,10000)
pivot_spot = 'high'
time1 = time.time()
quick_sort(0, len(arr3) - 1, arr3, pivot_spot, -1)
time2 = time.time()
#print(f'Sorted array: {arr3}')
print(f'Runtime: {time2-time1}')
set3.append({'n': 10000, 'pivot': pivot_spot, 'time': time2-time1, 'comp': ncomp})
print(f'Total comparisons: {ncomp}')
print("--------------------------------")

#Set 3, n=10000, pivot=random
print("--------------------------------")
print("Data Set #3: N = 1000, Random Pivot")
print("--------------------------------")
ncomp = 0
arr3 = numpy.random.randint(0,10000,10000)
pivot_spot = 'rand'
time1 = time.time()
quick_sort(0, len(arr3) - 1, arr3, pivot_spot, -1)
time2 = time.time()
#print(f'Sorted array: {arr3}')
print(f'Runtime: {time2-time1}')
set3.append({'n': 10000, 'pivot': pivot_spot, 'time': time2-time1, 'comp': ncomp})
print(f'Total comparisons: {ncomp}')
print("--------------------------------")


#Set 3, insertion sort hybrid): n=10000, pivot=random, threshold=10
print("--------------------------------")
print("Data Set #3: N = 1000, Insertion Sort")
print("--------------------------------")
ncomp = 0
arr3 = numpy.random.randint(0,10000,10000)
pivot_spot = 'rand'
time1 = time.time()
quick_sort(0, len(arr3) - 1, arr3, pivot_spot, threshold)
time2 = time.time()
#print(f'Sorted array: {arr3}')
print(f'Runtime: {time2-time1}')
set3.append({'n': 10000, 'pivot': pivot_spot, 'time': time2-time1, 'comp': ncomp})
print(f'Total comparisons: {ncomp}')
print("--------------------------------")



#df = pd.DataFrame({'n': arr1.size, 'Runtime': [time1 - time2]})
#print(tabulate(df, headers='keys',tablefmt='psql'))

