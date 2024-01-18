def find_repeated_elements(arr):
    n = len(arr)

    for i in range(n):
        if arr[abs(arr[i])] > 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            print(abs(arr[i]), end=" ")

# Example usage:
my_array = [1, 2, 3, 4, 2, 5, 6, 1, 7, 8, 9, 9]
print(find_repeated_elements(my_array))
