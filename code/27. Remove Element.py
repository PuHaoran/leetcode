class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] == val:
                t = nums[left]
                nums[left] = nums[right]
                nums[right] = t
                right -= 1
            else:
                left += 1
        return left

'''
题解：
时间复杂度O(n)，空间复杂度O(1)
数组左右两边各一个指针，若左边的数值等于val，则交换左右两边指针所指元素，同时右边指针左移；
若左边的数值不等于val，则左边指针右移，直至两指针相遇。
'''