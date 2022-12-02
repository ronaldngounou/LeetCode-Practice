class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = (nums1 + nums2)
        nums.sort()
        
        if len(nums)%2 != 0: #odd 
            middle = len(nums) // 2
            return nums[middle]
        else: #even
            middle = len(nums)/2
            print("middle", middle)
            
            print("n/2",nums[middle-1])
            print("n/2 + 1",nums[middle])
            print((2+3)/2)
            return (nums[middle-1] + nums[middle])/2.