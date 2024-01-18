def nth_highest(arr, n):
    arr.sort()
    return arr[-n]


def nth_highest1(arr, n):
    highest_values = [float('-inf')] * n

    for num in arr:
        for i in range(n):
            if num > highest_values[i]:
                for j in range(n - 1, i, -1):
                    highest_values[j] = highest_values[j - 1]
                highest_values[i] = num
                break

    return highest_values[-1]

# Example usage:
my_array = [3, 1, 5, 7, 9, 2, 6, 8, 4]
result = nth_highest(my_array, 4)
print("Second Highest Element:", result)

result1 = nth_highest1(my_array, 4)
print("Second Highest Element:", result1)
