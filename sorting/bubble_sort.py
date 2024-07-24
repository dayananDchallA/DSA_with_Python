from typing import List

class BubbleSort:
    def sort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Iterate through the list, reducing the range each time
        for i in range(n - 1):
            # Iterate through the unsorted part of the list
            for j in range(n - i - 1):
                # If the current element is greater than the next element, swap them
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

if __name__ == "__main__":
    lst_nums = [-1, 9, 12, 5, 0, 3]
    print("Original list:", lst_nums)  # Print the original list
    bs = BubbleSort()
    sorted_nums = bs.sort(lst_nums)
    print("Original list after sorting:", lst_nums)  # Print the original list again to show it is sorted
    print("Sorted list:", sorted_nums)  # Print the sorted list
