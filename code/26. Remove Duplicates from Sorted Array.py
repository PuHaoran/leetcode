class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)

        t = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[t]:
                t += 1
                nums[t] = nums[i]
        return t + 1

'''
题解：
考察数组
'''