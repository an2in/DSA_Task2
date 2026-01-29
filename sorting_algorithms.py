import random
import numpy as np


class SortingAlgorithms:
    """
    Sorting Algorithms Module

    This module contains implementations of various sorting algorithms:
    - QuickSort
    - HeapSort
    - MergeSort
    - NumPy Sort
    """
    
    @staticmethod
    def quicksort(arr):
        arr_copy = arr.copy()
        SortingAlgorithms._quicksort_recursive(arr_copy, 0, len(arr_copy) - 1)
        return arr_copy
    
    @staticmethod
    def _quicksort_recursive(arr, left, right):
        in_left_index = left
        in_right_index = right
        pivot = arr[left + random.randint(0, right - left)]

        while in_left_index <= in_right_index:
            while arr[in_left_index] < pivot:
                in_left_index += 1
            while arr[in_right_index] > pivot:
                in_right_index -= 1
            if in_left_index <= in_right_index:
                arr[in_left_index], arr[in_right_index] = arr[in_right_index], arr[in_left_index]
                in_left_index += 1
                in_right_index -= 1

        if left < in_right_index: SortingAlgorithms._quicksort_recursive(arr, left, in_right_index)
        if in_left_index < right: SortingAlgorithms._quicksort_recursive(arr, in_left_index, right)
    
    @staticmethod
    def heapsort(arr):
        arr_copy = arr.copy()
        arr_length = len(arr_copy)
        
        for i in range(arr_length // 2 - 1, -1, -1):
            SortingAlgorithms._heapify(arr_copy, arr_length, i)
        for i in range(arr_length - 1, 0, -1):
            arr_copy[i], arr_copy[0] = arr_copy[0], arr_copy[i]
            SortingAlgorithms._heapify(arr_copy, i, 0)
        return arr_copy
    
    @staticmethod
    def _heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            SortingAlgorithms._heapify(arr, n, largest)
    
    @staticmethod
    def mergesort(arr):
        arr_copy = arr.copy()
        SortingAlgorithms._mergesort_recursive(arr_copy)
        return arr_copy
    
    @staticmethod
    def _mergesort_recursive(arr):
        if len(arr) <= 1:
            return
        mid = len(arr) // 2
        left = arr[:mid].copy()
        right = arr[mid:].copy()

        SortingAlgorithms._mergesort_recursive(left)
        SortingAlgorithms._mergesort_recursive(right)

        SortingAlgorithms._merge(arr, left, right)
    
    @staticmethod
    def _merge(arr, left, right):
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    
    @staticmethod
    def numpy_sort(arr):
        return np.sort(arr, kind='quicksort')
