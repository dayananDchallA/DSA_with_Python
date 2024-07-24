from typing import List

'''
Explanation of Logic:
--------------------

Initialization:

n = len(nums): Get the length of the list.
fib_mm2 = 0: Initialize the (m-2)'th Fibonacci number.
fib_mm1 = 1: Initialize the (m-1)'th Fibonacci number.
fib_m = fib_mm2 + fib_mm1: Calculate the m'th Fibonacci number.

Finding the Smallest Fibonacci Number:

while fib_m < n: Find the smallest Fibonacci number greater than or equal to n.
Update fib_mm2, fib_mm1, and fib_m in each iteration.

Main Search Loop:

offset = -1: Initialize the offset, marking the eliminated range from the front.
while fib_m > 1: Continue searching while there are elements to be inspected.
i = min(offset + fib_mm2, n - 1): Check if fib_mm2 is a valid index.

Comparison and Range Adjustment:

if nums[i] < target: If the target is greater than the value at index fib_mm2, update the range to search.
Update fib_m, fib_mm1, fib_mm2, and offset.
elif nums[i] > target: If the target is less than the value at index fib_mm2, update the range to search.
Update fib_m, fib_mm1, and fib_mm2.
else: If the target is found at the calculated position, return the position.

Final Comparison:

if fib_mm1 and nums[offset + 1] == target: Compare the last element with the target.
return offset + 1: If the target is found, return the index.

Result:

return -1: If the target is not found, return -1 indicating the target is not in the list.
'''

class FibonacciSearch:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)  # Get the length of the list
        fib_mm2 = 0  # (m-2)'th Fibonacci Number
        fib_mm1 = 1  # (m-1)'th Fibonacci Number
        fib_m = fib_mm2 + fib_mm1  # m'th Fibonacci Number

        # Find the smallest Fibonacci number greater than or equal to n
        while fib_m < n:
            fib_mm2 = fib_mm1
            fib_mm1 = fib_m
            fib_m = fib_mm2 + fib_mm1

        offset = -1  # Marks the eliminated range from front

        # While there are elements to be inspected
        while fib_m > 1:
            # Check if fib_mm2 is a valid index
            i = min(offset + fib_mm2, n - 1)

            # If target is greater than the value at index fib_mm2, cut the subarray from offset to i
            if nums[i] < target:
                fib_m = fib_mm1
                fib_mm1 = fib_mm2
                fib_mm2 = fib_m - fib_mm1
                offset = i

            # If target is less than the value at index fib_mm2, cut the subarray after i+1
            elif nums[i] > target:
                fib_m = fib_mm2
                fib_mm1 = fib_mm1 - fib_mm2
                fib_mm2 = fib_m - fib_mm1

            # Element found. Return index.
            else:
                return i

        # Comparing the last element with target
        if fib_mm1 and nums[offset + 1] == target:
            return offset + 1

        # Element not found. Return -1
        return -1

if __name__ == "__main__":
    nums = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]  # Example list
    target = 85  # Element to search for
    fs = FibonacciSearch()  # Create an instance of FibonacciSearch
    result = fs.search(nums, target)  # Perform Fibonacci search
    print(f"Element {target} is at index: {result}")  # Print the result
