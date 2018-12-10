# -*- coding: utf-8 -*-

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallestIndex = findSmallest(arr)
        smallestItem = arr.pop(smallestIndex)
        newArr.append(smallestItem)
    return newArr


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

originArr = [7, 5, 9, 3, 2, 6]
print(selectionSort(originArr))
