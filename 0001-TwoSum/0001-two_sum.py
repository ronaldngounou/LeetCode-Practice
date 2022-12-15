class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hash_table= {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in hash_table:
                hash_table[nums[i]] = i
            else:
                return [hash_table[complement], i] 
