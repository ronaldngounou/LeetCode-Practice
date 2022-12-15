class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        output = []
        for i in range(0, len(nums)): 
            count = 0
            for j in range(len(nums)-1, -1,-1): 
                # Distinct elements
                if nums[j] < nums[i] and i!=j:
                    count += 1
                else: 
                    j -=1
            output.append(count)
        return output
