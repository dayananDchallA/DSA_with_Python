from typing import List

'''
Explanation of Logic:
--------------------

Initialization:

left, right = 0, len(nums) - 1: Set the initial boundaries of the search range to cover the entire list.

Main Loop:

while left <= right: Continue searching as long as the search range is valid (i.e., left does not exceed right).

Mid Calculation:

mid = left + (right - left) // 2: Calculate the middle index to avoid potential overflow issues. This is safer than (left + right) // 2 in languages with fixed integer sizes.

Comparison:
if nums[mid] == target: If the middle element is the target, return its index.
elif nums[mid] < target: If the target is greater than the middle element, adjust the left boundary to search the right half.
else: If the target is less than the middle element, adjust the right boundary to search the left half.

Result:

return -1: If the loop exits without finding the target, return -1 to indicate the target is not in the list.
'''

class BinarySearch:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # Initialize pointers to the start and end of the list
        while left <= right:
            mid = left + (right - left) // 2  # Calculate the mid index to avoid potential overflow
            if nums[mid] == target:
                return mid  # If the target is found, return the index
            elif nums[mid] < target:
                left = mid + 1  # If the target is greater, ignore the left half
            else:
                right = mid - 1  # If the target is smaller, ignore the right half
        return -1  # If the target is not found, return -1
    
if __name__ == "__main__":
    lst_nums=[-1,0,3,5,9,12]
    bs = BinarySearch()
    target = 6
    result = bs.search(lst_nums, target)
    print(f"Element {target} is at index: {result}")
            
