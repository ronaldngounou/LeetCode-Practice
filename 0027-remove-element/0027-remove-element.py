class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        
        return len(nums)
        
        
        # for i in range(len(nums)-1, -1, -1):
        #     if nums[i] == val:
        #         nums.pop(i)
        # return len(nums)
        

        