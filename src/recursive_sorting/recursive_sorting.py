# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    arr = arrA + arrB
    for i in range(0, len(arr)-1):
        cur_index = i  # [*1*, 5, 8, 4] = 0 index
        # save smallest value
        smallest_index = cur_index  # 0 index

        for j in range(cur_index, len(arr)):
            # compare the current smallest value to the rest of array
            # if there is a smaller item then set the smallest_index = that item
            if arr[smallest_index] > arr[j]:  # [1, *5*, 8, *4* ]
                # if there is a smaller item than the current save it
                smallest_index = j  # index 1 now-> index 3

        # swap bigger values to the right and smaller to left
        temp = arr[smallest_index]  # [1, 5, 8, *4*]
        # smaller value = current value (we move the bigger to the right)
        arr[smallest_index] = arr[cur_index]  # [1, *5, 8, *4] => [1, 5, 8, 5]
        # Set current value to equal the smaller (left = smaller)
        arr[cur_index] = temp  # [1, 5, 8, 5] => [1, 4, 8, 5]

    return arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):

    arr1 = []
    arr2 = []
    # if the array is still bigger than 1 split
    if len(arr) > 1:
        # middle of the array rounded
        middle = int(len(arr) / 2)
        # first half
        arr1 = arr[:middle]
        # second half
        arr2 = arr[middle:]

        # recursive
        merge_sort(arr1)
        merge_sort(arr2)

        # Start merging

    return arr


# # STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r):
#     # TO-DO

#     return arr


# # STRETCH: implement the Timsort function below
# # hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr
