from typing import List

class HeapSort:
    def sort(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Build a maxheap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(nums, n, i)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, i, 0)

        return nums

    def heapify(self, nums: List[int], n: int, i: int):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and nums[i] < nums[left]:
            largest = left

        if right < n and nums[largest] < nums[right]:
            largest = right

        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.heapify(nums, n, largest)

if __name__ == "__main__":
    lst_nums = [4, 10, 3, 5, 1]
    print("Original list:", lst_nums)
    hs = HeapSort()
    sorted_nums = hs.sort(lst_nums)
    print("Sorted list:", sorted_nums)
