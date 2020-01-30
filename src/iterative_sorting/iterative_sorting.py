# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(1, len(arr)):
        j = i
        # 1st while j is greater or equal than 0 since we are counting down
        # 2nd while item on rigth is smaller than left item (continue)
        while j > 0 and arr[j] < arr[j-1]:
            #saving current value
            temp = arr[j]  # [1, 5, 8, *4*]

            #right = left
            arr[j] = arr[j - 1]  # [1, 5, 8, 4] => [1, 5, 8, 8]

            #left = original value
            arr[j-1] = temp  # [1, 5, 8, 8] => [1, 5, 4, 8]

            #decrease the value of j to eventually terminate loop
            j -= 1
    return arr        



# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr


arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
selection_sort(arr)
