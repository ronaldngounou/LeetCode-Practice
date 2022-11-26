class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        div_max = []
        div_min = []

        for i in range(1, max(nums)+1):
            if max(nums)%i == 0:
                div_max.append(i)
            if min(nums)%i == 0:
                div_min.append(i)
        print(div_max)
        print(div_min)

        common = []
        for elem in div_max:
            if elem in div_min:
                common.append(elem)
        return max(common)
  
        