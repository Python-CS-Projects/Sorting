# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(0, len(arr)-1):
        cur_index = i  # [*1*, 5, 8, 4] = 0 index
        #save smallest value
        smallest_index = cur_index  # 0 index

        for j in range(cur_index, len(arr)):
            #compare the current smallest value to the rest of array
            #if there is a smaller item then set the smallest_index = that item
            if arr[smallest_index] > arr[j]:  # [1, *5*, 8, *4* ]
              #if there is a smaller item than the current save it
              smallest_index = j  # index 1 now-> index 3

        #swap bigger values to the right and smaller to left
        temp = arr[smallest_index]  # [1, 5, 8, *4*]
        arr[smallest_index] = arr[cur_index]  # [1, *5, 8, *4] => [1, 5, 8, 5]
        arr[cur_index] = temp  # [1, 5, 8, 5] => [1, 4, 8, 5]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # loop through n-1 elements
    for i in range(1, len(arr)):
        j = i
        # 1st while j is greater or equal than 0 since we are counting down
        # 2nd while item on rigth is smaller than left item (continue)
        while j > 0 and arr[j] < arr[j-1]:
            # saving current value
            temp = arr[j]  # [1, 5, 8, *4*]

            #right = left
            arr[j] = arr[j - 1]  # [1, 5, 8, 4] => [1, 5, 8, 8]

            # left = original value
            arr[j-1] = temp  # [1, 5, 8, 8] => [1, 5, 4, 8]

            # decrease the value of j to eventually terminate loop
            j -= 1
    return arr


# STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):


#     return arr

