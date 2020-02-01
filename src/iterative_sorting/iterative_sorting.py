# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
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


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(0, len(arr)):  # range(start,stop,step)
        # print(i)
        for j in range(0, len(arr)-1):  # iterate from 0-current index of i ex 0-9
            # if item on the left is greater than item on the right then *swap*
            if arr[j] > arr[j+1]:  # [*5L* > *8R*, 4, 2] then swap

                temp = arr[j]  # [*5*, 8, 4, 2]
                arr[j] = arr[j+1]  # [5 <- 8, 4, 2] = [8, 8, 4, 2]
                arr[j+1] = temp  # [8, 8, 4, 2] = [8, 5, 4, 2]
    return arr


# STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):


#     return arr
