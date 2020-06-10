# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Example 1:
#
# Input: [1,3,5,6], 5
# Output: 2
# Example 2:
#
# Input: [1,3,5,6], 2
# Output: 1

import bisect

def searchInsert(nums, target):
    # if target in nums:
    #     return nums.index(target)
    # else:
    #     bisect.insort(nums, target)
    #     return nums.index(target)
    lo = 0
    hi = len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo



print(searchInsert([1,3,5,6], 3))