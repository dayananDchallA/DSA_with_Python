from typing import List

class MergeSort:
    def sort(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            mid = len(nums) // 2
            left_half = nums[:mid]
            right_half = nums[mid:]

            # Recursively sort both halves
            self.sort(left_half)
            self.sort(right_half)

            i = j = k = 0

            # Merge the sorted halves
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    nums[k] = left_half[i]
                    i += 1
                else:
                    nums[k] = right_half[j]
                    j += 1
                k += 1

            # Copy any remaining elements of left_half
            while i < len(left_half):
                nums[k] = left_half[i]
                i += 1
                k += 1

            # Copy any remaining elements of right_half
            while j < len(right_half):
                nums[k] = right_half[j]
                j += 1
                k += 1

        return nums

if __name__ == "__main__":
    lst_nums = [-1, 9, 12, 5, 0, 3]
    print("Original list:", lst_nums)
    ms = MergeSort()
    sorted_nums = ms.sort(lst_nums)
    print("Sorted list:", sorted_nums)
