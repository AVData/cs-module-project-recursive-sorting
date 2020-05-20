# TO-DO: complete the helper function below to merge 2 sorted arrays
from math import floor


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []
#    merged_arr = [0] * elements

    # Your code here
    # compare first elements of arrA and arrB
    # remove the smaller from arrA or arrB and put into merged_arr
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] >= arrB[0]:
            merged_arr.append(arrB.pop(0))
            print(merged_arr)
        else:
            merged_arr.append(arrA.pop(0))
            print(merged_arr)

    # handle any leftover list elements
    while len(arrA) > 0:
        merged_arr.append(arrA.pop(0))
    while len(arrB) > 0:
        merged_arr.append(arrB.pop(0))

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
# split thearray here
def merge_sort(arr):
    # Your code here

    if len(arr) <= 1:
        return arr

    midpoint = floor(len(arr)/2)
    left = arr[:midpoint]
    right = arr[midpoint:]

    left = merge_sort(left)
    right = merge_sort(right)

    arr = merge(left, right)
    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    pointer1 = start+1
    if arr[start] <= arr[pointer1]:
        return arr
    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if len(arr) <= 1:
        return arr

    midpoint = floor((r-l)/2)
    merge_sort_in_place(arr, l, midpoint)
    merge_sort_in_place(arr, midpoint, r)

    merge_in_place(arr, l, midpoint, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):
#     # Your code here
#
#     return arr
