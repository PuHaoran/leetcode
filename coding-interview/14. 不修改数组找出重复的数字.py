'''
给定一个长度为 n+1 的数组nums，数组中所有的数均在 1∼n 的范围内，其中 n≥1。

请找出数组中任意一个重复的数，但不能修改输入的数组。

样例
给定 nums = [2, 3, 5, 4, 3, 2, 6, 7]。

返回 2 或 3。
思考题：如果只能使用 O(1) 的额外空间，该怎么做呢？
'''

class Solution(object):
    def duplicateInArray(self, nums):
        """
        :type nums: List[int]
        :rtype int
        """
        start = 1
        end = len(nums) - 1
        while 1:
            mid = (start + end)//2
            cnt = 0
            for i in range(len(nums)):
                if nums[i] >= start and nums[i] <= mid:
                    cnt += 1
            if cnt > (mid - start + 1):
                end = mid
                if start == end:
                    return start
            else:
                start = mid + 1

'''
题解:
采用二分法进行解答，在1~N的范围内，数组长度却有N+1，说明必有1至少一个重复值；
然后进行二分，若在值范围内数组长度不合理则继续二分，直到找到只有一个值的情况。
'''