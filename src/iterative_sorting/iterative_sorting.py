# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(1, len(arr) - 1):
        arr_len = len(arr) - 1
        cur_index = i
        ordered_value = arr[0]
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        if cur_index < arr_len:
            print("Bigger index")

        # TO-DO: swap

    print("done")


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
selection_sort(arr)
