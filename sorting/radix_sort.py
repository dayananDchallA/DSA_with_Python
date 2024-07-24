from typing import List

class RadixSort:
    def sort(self, nums: List[int]) -> List[int]:
        max_val = max(nums)
        exp = 1
        while max_val // exp > 0:
            self.counting_sort(nums, exp)
            exp *= 10
        return nums

    def counting_sort(self, nums: List[int], exp: int):
        n = len(nums)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = nums[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            index = nums[i] // exp
            output[count[index % 10] - 1] = nums[i]
            count[index % 10] -= 1

        for i in range(len(nums)):
            nums[i] = output[i]

if __name__ == "__main__":
    lst_nums = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original list:", lst_nums)
    rs = RadixSort()
    sorted_nums = rs.sort(lst_nums)
    print("Sorted list:", sorted_nums)
