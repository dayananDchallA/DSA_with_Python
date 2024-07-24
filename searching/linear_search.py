from typing import List

'''
Explanation of Logic:
--------------------

Linear Search Method:

def search(self, nums: List[int], target: int) -> int: Define the method search with parameters nums (a list of integers) and target (the integer to search for).
for index, value in enumerate(nums): Iterate through the list, obtaining both the index and value of each element.
if value == target: Check if the current value matches the target.
return index: If a match is found, return the index of the target.
return -1: If the target is not found after iterating through the list, return -1 indicating the target is not in the list.
'''

class LinearSearch:
    def search(self, nums: List[int], target: int) -> int:
        # Iterate through the list with both index and value
        for index, value in enumerate(nums):
            # If the current value matches the target, return the index
            if value == target:
                return index
        # If the target is not found, return -1
        return -1

if __name__ == "__main__":
    nums = [4, 2, 5, 1, 3]  # Example list
    target = 5  # Element to search for
    ls = LinearSearch()  # Create an instance of LinearSearch
    result = ls.search(nums, target)  # Perform linear search
    print(f"Element {target} is at index: {result}")  # Print the result
