from typing import List

class CountingSort:
    def sort(self, nums: List[int]) -> List[int]:
        max_val = max(nums)
        min_val = min(nums)
        range_of_elements = max_val - min_val + 1
        count = [0] * range_of_elements
        output = [0] * len(nums)

        # Store count of each character
        for num in nums:
            count[num - min_val] += 1

        # Change count[i] so that count[i] now contains actual
        # position of this character in output array
        for i in range(1, len(count)):
            count[i] += count[i - 1]

        # Build the output character array
        for i in range(len(nums) - 1, -1, -1):
            output[count[nums[i] - min_val] - 1] = nums[i]
            count[nums[i] - min_val] -= 1

        # Copy the output array to nums
        for i in range(len(nums)):
            nums[i] = output[i]

        return nums

if __name__ == "__main__":
    lst_nums = [4, 2, 2, 8, 3, 3, 1]
    print("Original list:", lst_nums)
    cs = CountingSort()
    sorted_nums = cs.sort(lst_nums)
    print("Sorted list:", sorted_nums)
