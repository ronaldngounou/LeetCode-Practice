class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        z = nums[-1]
        w = nums[0]
        y = nums[-2]
        x = nums[1]
        return ((z*y) - (x*w))