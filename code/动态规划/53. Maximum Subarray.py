"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _min = 0
        res = nums[0]
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s - _min > res:
                res = s - _min
            if s < _min:
                _min = s
        return res

"""
题解：
求最大子串问题
这道题被归结到了dp问题中，但其实更容易想到的是数学解法。
最大子串 = 数组当前和 - 当前位置之前的数组最小和
"""