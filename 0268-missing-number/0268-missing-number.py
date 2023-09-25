class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            freq[nums[i]] += 1 
        for i in range(len(freq)):
            if freq[i] == 0:
                return i 



        