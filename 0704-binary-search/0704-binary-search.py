class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        high = len(nums)-1 
        low = 0

        while low<=high:
            index = (high + low) // 2
            if target > nums[index]:
                low = index + 1
            elif target < nums[index]:
                high = index -1 
            else:
                return index
        return -1