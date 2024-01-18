def majority_element(nums):
    if len(nums) == 0:
        return None
    count = 1
    candidate = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == candidate:
            count += 1
        else:
            count -= 1
        if count == 0:
            candidate = nums[i]
            count = 1
    return candidate


print(majority_element([3, 2, 3]))