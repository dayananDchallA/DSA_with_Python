from typing import List

class QuickSort:
    def sort(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums: List[int], low: int, high: int):
        if low < high:
            pi = self.partition(nums, low, high)
            self.quick_sort(nums, low, pi - 1)
            self.quick_sort(nums, pi + 1, high)

    def partition(self, nums: List[int], low: int, high: int) -> int:
        pivot = nums[high]
        i = low - 1
        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

if __name__ == "__main__":
    lst_nums = [10, 1, 8, 6, 4, 7, 9, 2, 3, 5]
    print("Original list:", lst_nums)
    qs = QuickSort()
    sorted_nums = qs.sort(lst_nums)
    print("Sorted list:", sorted_nums)
