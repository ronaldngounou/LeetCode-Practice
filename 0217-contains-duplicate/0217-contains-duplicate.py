class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique = set()
        for num in nums:
            if num not in unique:
                unique.add(num)
            else:
                return True
        return False 