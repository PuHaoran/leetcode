'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。

输入一个升序的数组的一个旋转，输出旋转数组的最小元素。

例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。

数组可能包含重复项。

注意：数组内所含元素非负，若数组大小为0，请返回-1。

样例
输入：nums=[2,2,2,0,1]

输出：0
'''


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        i = 0
        j = len(nums) - 1
        while 1:
            if i + 1 > len(nums) - 1 or j - 1 < 0:
                break
            if nums[i] <= nums[i + 1]:
                i += 1
            else:
                return nums[i + 1]

            if nums[j] >= nums[j - 1]:
                j -= 1
            else:
                return nums[j]

        return nums[0]

'''
题解：
根据旋转数组左边递增，右边递减的性质解答，每次遍历同时比较左右两边，找到不满足则停止遍历。
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        _min = nums[0]
        for i in range(len(nums)):
            if nums[i] < _min:
                _min = nums[i]
        return _min

'''
解答：
直接遍历取最小值也能A掉。
'''