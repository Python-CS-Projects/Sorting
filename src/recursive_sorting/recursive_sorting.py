# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    index = 0
    for i in range(merge_arr)
     # 3.LHS is empty
     if len(arrA) == 1:
        # copy RHS to the merged_arr
        merged_arr[i] = arrA[0]
      # 4.RHS is empty
      elif len(arrB) == 1:
        # copy LHS to the merged_arr
         merged_arr[i] = arrB[0]
    # 1.front of LHS < front of RHS
      elif arrA[0] < arrB[0]:
        merged_arr[i] = arrA[0]
        arrA.pop(0)
    # 2.front of RHS < front of LHS
      elif arrA[0] < arrB[0]:
        merged_arr[i] = arrB[0]
        arrB.pop(0)
    return arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):

    arr1 = []
    arr2 = []
    # if the array is still bigger than 1 split

    if len(arr) > 1:
      return arr
    else:
        # middle of the array rounded
        middle = len(arr) // 2
        # first half
        arr1 = arr[:middle]
        # second half
        arr2 = arr[middle:]
        # recursive
        merge_sort(arr1)
        merge_sort(arr2)
        # Start merging by invoking the above method
        merge(arr1,arr2)
 



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
