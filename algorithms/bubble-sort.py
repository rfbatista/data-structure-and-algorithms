def bubble_sort(arr):
    for i, _ in enumerate(arr):
        for j, _ in enumerate(arr[i:-1]):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

print(bubble_sort([1,122,5,2,3,4,10]))
