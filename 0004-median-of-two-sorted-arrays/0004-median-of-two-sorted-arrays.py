class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = (nums1 + nums2)
        nums.sort()
        
        if len(nums)%2 != 0: #odd number of elements
            middle = len(nums) // 2
            return nums[middle]
        
        else: #even number of elements
            middle = len(nums)/2
            print("middle", middle)
            
            
            print("middle", nums[middle-1]) #-1 because index in the list starts from 0
            print("after the middle",nums[middle])
            print((2+3)/2)
            
            return (nums[middle-1] + nums[middle])/2.   #notice the point to float the value. 