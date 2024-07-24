from typing import List
'''
Explanation of Logic:
--------------------

Search Method:

if nums[0] == target: Check if the target is at the first position. If so, return 0.
index = 1: Initialize the index to 1.
while index < len(nums) and nums[index] <= target: Exponentially increase the index until it exceeds the length of the list or the target is smaller than the current element.
return self.binary_search(nums[:min(index, len(nums))], target): Perform binary search in the identified range. The range is limited to the smaller value between index and the length of the list to avoid out-of-bounds errors.

Binary Search Method:

left, right = 0, len(nums) - 1: Initialize pointers to the start and end of the list.
while left <= right: Continue searching while the search range is valid (i.e., left does not exceed right).
mid = (left + right) // 2: Calculate the middle index.
if nums[mid] == target: If the target is found at the middle index, return mid.
elif nums[mid] < target: If the target is greater than the middle element, adjust the left boundary to search the right half.
else: If the target is less than the middle element, adjust the right boundary to search the left half.
return -1: If the loop exits without finding the target, return -1 to indicate the target is not in the list.
'''


class ExponentialSearch:
    def search(self, nums: List[int], target: int) -> int:
        # Check if the target is at the first position
        if nums[0] == target:
            return 0

        # Initialize the index to 1
        index = 1

        # Exponentially increase the index until the end of the list or the target is smaller than the current element
        while index < len(nums) and nums[index] <= target:
            index *= 2

        # Perform binary search in the identified range
        return self.binary_search(nums[:min(index, len(nums))], target)

    def binary_search(self, nums: List[int], target: int) -> int:
        # Initialize pointers to the start and end of the list
        left, right = 0, len(nums) - 1
        
        # Continue searching while the search range is valid
        while left <= right:
            # Calculate the mid index
            mid = (left + right) // 2
            
            # Check if the target is found
            if nums[mid] == target:
                return mid
            
            # If the target is greater, ignore the left half
            elif nums[mid] < target:
                left = mid + 1
            
            # If the target is smaller, ignore the right half
            else:
                right = mid - 1
        
        # If the target is not found, return -1
        return -1

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 7
    es = ExponentialSearch()
    result = es.search(nums, target)
    print(f"Element {target} is at index: {result}")
