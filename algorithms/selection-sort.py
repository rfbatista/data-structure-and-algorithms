def findsmallest(arr):
  smallest = arr[0]
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index

def selection_sort(arr):
  newArr = []
  for i in range(len(arr)):
    smallestIndex = findsmallest(arr)
    newArr.append(arr.pop(smallestIndex))
  return newArr

print(selection_sort([5,23,3,1,43,10]))