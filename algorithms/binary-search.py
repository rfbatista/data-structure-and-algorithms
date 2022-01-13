def binary_search(list, item):
	low = 0
	high = len(list) - 1
	while low <= high:
		mid = (low + high)//2
		guess = list[mid]
		print(high, low, mid, guess)
		if guess == item:
			return mid
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None

my_list = [1, 3, 5, 7, 9, 11, 12, 13, 14, 15, 16]

print("\nFirst try:")
print(binary_search(my_list, 9))

print("\nSecond try")
print(binary_search(my_list, -1)) 