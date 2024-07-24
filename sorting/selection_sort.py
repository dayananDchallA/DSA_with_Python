from typing import List

class SelectionSort:
    def sort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Iterate through each element of the list
        for i in range(n):
            # Assume the current element is the smallest
            min_index = i
            # Find the smallest element in the remaining unsorted part of the list
            for j in range(i + 1, n):
                if nums[min_index] > nums[j]:
                    # Update the index of the smallest element
                    min_index = j
            # Swap the found smallest element with the current element
            nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums

if __name__ == "__main__":
    lst_nums = [10, 1, 8, 6, 4, 7, 9, 2, 3, 5]
