from typing import List

class BucketSort:
    def sort(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return nums

        bucket_size = 10
        min_value = min(nums)
        max_value = max(nums)
        bucket_count = (max_value - min_value) // bucket_size + 1
        buckets = [[] for _ in range(bucket_count)]

        for num in nums:
            buckets[(num - min_value) // bucket_size].append(num)

        nums.clear()
        for bucket in buckets:
            bucket.sort()
            nums.extend(bucket)

        return nums

if __name__ == "__main__":
    lst_nums = [29, 25, 3, 49, 9, 37, 21, 43]
    print("Original list:", lst_nums)
    bs = BucketSort()
    sorted_nums = bs.sort(lst_nums)
    print("Sorted list:", sorted_nums)
