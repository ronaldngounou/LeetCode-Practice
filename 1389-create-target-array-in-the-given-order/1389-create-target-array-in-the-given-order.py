class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target = []
        
        for i in range (0, len(nums)):
            target.insert(index[i], nums[i])
            
        return target
        
    
        
        
        
        