import math
from typing import List

'''
Explanation of Logic:
--------------------

Initialization:

n = len(nums): Get the length of the list.
step = int(math.sqrt(n)): Calculate the optimal jump step size using the square root of the length of the list.
prev = 0: Initialize the previous step to 0.

Jump Search Loop:

while nums[min(step, n) - 1] < target: Jump through the list in blocks until reaching the end of the list or until the target is less than the current element.
prev = step: Update the previous step.
step += int(math.sqrt(n)): Jump forward by the step size.
if prev >= n: If the previous step exceeds the length of the list, return -1 indicating the target is not found.

Linear Search in the Block:

for i in range(prev, min(step, n)): Perform a linear search within the identified block.
if nums[i] == target: If the target is found, return the index.

Result:

return -1: If the target is not found in the block, return -1 indicating the target is not in the list.

'''

class JumpSearch:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)  # Get the length of the list
        step = int(math.sqrt(n))  # Calculate the optimal jump step size
        prev = 0  # Initialize the previous step to 0

        # Jump through the list in blocks until the end of the list or the target is less than the current element
        while nums[min(step, n) - 1] < target:
            prev = step  # Update the previous step
            step += int(math.sqrt(n))  # Jump forward by the step size
            if prev >= n:  # If the previous step exceeds the length of the list, return -1
                return -1

        # Perform linear search in the identified block
        for i in range(prev, min(step, n)):
            if nums[i] == target:  # If the target is found, return the index
                return i

        # If the target is not found, return -1
        return -1

if __name__ == "__main__":
    nums = [0, 1, 2, 4, 5, 7, 9, 10, 12, 15]  # Example list
    target = 10  # Element to search for
    js = JumpSearch()  # Create an instance of JumpSearch
    result = js.search(nums, target)  # Perform jump search
    print(f"Element {target} is at index: {result}")  # Print the result
