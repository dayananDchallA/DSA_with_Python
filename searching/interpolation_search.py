from typing import List

'''
Explanation of Logic:
--------------------

Initialization:

low, high = 0, len(nums) - 1: Initialize pointers to the start (low) and end (high) of the list.

Interpolation Search Loop:

while low <= high and target >= nums[low] and target <= nums[high]: Continue searching while the range is valid and the target is within the range.
if low == high: Check if the search range has reduced to a single element.
if nums[low] == target: If the target is found at the single element, return the index.
return -1: If the target is not found, return -1.

Position Calculation:

pos = low + ((target - nums[low]) * (high - low) // (nums[high] - nums[low])): Calculate the position using the interpolation formula.

Comparison and Boundary Adjustment:

if nums[pos] == target: If the target is found at the calculated position, return the position.
if nums[pos] < target: If the target is greater than the element at the calculated position, adjust the lower bound (low) to search the right subarray.
else: If the target is smaller than the element at the calculated position, adjust the upper bound (high) to search the left subarray.

Result:

return -1: If the target is not found, return -1 indicating the target is not in the list.
'''

class InterPolationSearch:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1  # Initialize pointers to the start and end of the list

        # Continue searching while the range is valid and the target is within the range
        while low <= high and target >= nums[low] and target <= nums[high]:
            # If the search range has reduced to a single element
            if low == high:
                if nums[low] == target:
                    return low  # Return the index if the target is found
                return -1  # Return -1 if the target is not found

            # Calculate the position using the interpolation formula
            pos = low + ((target - nums[low]) * (high - low) // (nums[high] - nums[low]))

            # If the target is found at the calculated position, return the position
            if nums[pos] == target:
                return pos

            # If the target is greater, adjust the lower bound to search the right subarray
            if nums[pos] < target:
                low = pos + 1
            # If the target is smaller, adjust the upper bound to search the left subarray
            else:
                high = pos - 1

        # If the target is not found, return -1
        return -1

if __name__ == "__main__":
    nums = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]  # Example list
    target = 18  # Element to search for
    ips = InterPolationSearch()  # Create an instance of InterPolationSearch
    result = ips.search(nums, target)  # Perform interpolation search
    print(f"Element {target} is at index: {result}")  # Print the result
