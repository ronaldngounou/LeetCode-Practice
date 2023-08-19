class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        score = 0
        nums = sorted(nums)
        for i in range(k):
            score += nums[len(nums)-1]
            nums[len(nums)-1] += 1
        return score