from typing import List

class ShellSort:
    def sort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = nums[i]
                j = i
                while j >= gap and nums[j - gap] > temp:
                    nums[j] = nums[j - gap]
                    j -= gap
                nums[j] = temp
            gap //= 2

        return nums

if __name__ == "__main__":
    lst_nums = [12, 34, 54, 2, 3]
    print("Original list:", lst_nums)
    ss = ShellSort()
    sorted_nums = ss.sort(lst_nums)
    print("Sorted list:", sorted_nums)
