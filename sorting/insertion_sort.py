from typing import List

class InsertionSort:
    def sort(self, nums: List[int]) -> List[int]:
        # Iterate from the second element to the end of the list
        for i in range(1, len(nums)):
            # The current element to be inserted into the sorted part of the list
            key = nums[i]
            # Start comparing with the element just before the current element
            j = i - 1
            # Shift elements of the sorted part to the right until the correct position for the key is found
            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            # Insert the current element into its correct position
            nums[j + 1] = key
        return nums

if __name__ == "__main__":
    lst_nums = [-1, 9, 12, 5, 0, 3]
    print("Original list:", lst_nums)  # Print the original list
    isort = InsertionSort()
    sorted_nums = isort.sort(lst_nums)
    print("Original list after sorting:", lst_nums)  # Print the original list again to show it is sorted
    print("Sorted list:", sorted_nums)  # Print the sorted list
