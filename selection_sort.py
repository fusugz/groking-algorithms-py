# -*- coding: utf-8 -*-

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallestIndex = findSmallest(arr)
        newArr.append(arr.pop(smallestIndex))
    return newArr

originArr = [7, 5, 9, 3, 2, 6]
print(selectionSort(originArr))
