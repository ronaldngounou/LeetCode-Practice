class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        gcd = 1 
    
        for i in range(1 ,min(nums)+1):
            if min(nums) % i == 0 and max(nums) % i ==0:
                gcd = i
        return gcd
    
#         div_max = []
#         div_min = []

#         for i in range(1, max(nums)+1):
#             if max(nums)%i == 0:
#                 div_max.append(i)
#             if min(nums)%i == 0:
#                 div_min.append(i)

#         common = []
#         for elem in div_max:
#             if elem in div_min:
#                 common.append(elem)
#         return max(common)
        
