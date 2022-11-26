class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Check if nums is elsewhere in the list
        for num in nums:
            if nums.count(num) == 1:
                return num
                
            
    
            
        