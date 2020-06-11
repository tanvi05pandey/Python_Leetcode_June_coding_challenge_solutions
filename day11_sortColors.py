"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color
are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""



def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    beg, mid, end = 0, 0, len(nums) - 1

    while mid <= end:
        if nums[mid] == 0:
            nums[beg], nums[mid] = nums[mid], nums[beg]
            mid += 1
            beg += 1
        elif nums[mid] == 2:
            nums[mid], nums[end] = nums[end], nums[mid]
            end -= 1
        else:  #nums[mid] == 1:
            mid += 1
    #return nums


print(sortColors([2,0,2,1,1,0]))
