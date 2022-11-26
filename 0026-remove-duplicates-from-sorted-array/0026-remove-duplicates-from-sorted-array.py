class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """       
    
        
        high_value=nums[-1]
        i=1
        while i<len(nums):
            if nums[i] == nums[i-1]:
                value = nums.pop(i)
                # after I popped, I need to update the indexes to come back again and check the loop 
                i-=1
                nums.append(value) 
            if nums[i] == high_value:
                return i+1
            i += 1
                
                
            
    
            
            