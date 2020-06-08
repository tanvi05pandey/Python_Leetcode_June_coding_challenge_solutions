# Given an array w of positive integers, where w[i] describes the weight of index i,
# write a function pickIndex which randomly picks an index in proportion to its weight.
#
# Note:
#
# 1 <= w.length <= 10000
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10000 times.
# Example 1:
#
# Input:
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output: [null,0]
#
# Example 2:
#
# Input:
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]
import random


class Solution:

    def __init__(self, w):
        self.cumulative_sum = []
        self.total = 0
        for item in w:
            self.total += item
            self.cumulative_sum.append(self.total)

    def pickIndex(self) -> int:
        random_num = random.random() * self.total
        low, high = 0, len(self.cumulative_sum)
        while low < high:
            mid = low + (high - low)//2
            if random_num > self.cumulative_sum[mid]:
                low = mid + 1
            else:
                high = mid
        print(low)


obj = Solution([1,3,4])
param_1 = obj.pickIndex()
