class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        #the first and second number and the last number. As the array is sorted, there couldn't be any numbers between that could be bigger than the last one.
        max1 = nums[0]*nums[1]*nums[-1]

        #return the last three numbers if we have only positive numbers
        max2 = nums[-3]*nums[-2]*nums[-1]

        #in either cases, return the maximum of the two numbers
        return max(max1, max2)
