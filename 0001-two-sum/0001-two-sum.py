class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hash_table = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_table:
                return [hash_table[complement], i]
            else:
                hash_table[num] = i
        
                