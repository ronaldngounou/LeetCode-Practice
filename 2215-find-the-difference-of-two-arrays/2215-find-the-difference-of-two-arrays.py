class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        temp_diff = [[]]
        
        for num in nums1:
            if num not in nums2 and num not in temp_diff[0]:
                temp_diff[0].append(num)     
        diff = []
        for num in nums2:
            if num not in nums1 and num not in diff:
                diff.append(num)
        temp_diff.append(diff)
        return temp_diff

        
    

        