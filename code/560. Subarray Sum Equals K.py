'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
'''


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        d = collections.defaultdict(int)

        s = 0
        res = 0
        d[0] = 1
        for i in range(len(nums)):
            s += nums[i]
            if s - k in d:
                res += d[s - k]
            d[s] += 1
        return res

'''
题解:
以空间换时间，很巧妙的解法，时间复杂度和空间复杂度均为O(n)。
'''