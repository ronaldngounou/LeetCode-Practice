class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        strs = [str(digit) for digit in digits]
        
        int_digits = int("".join(strs)) + 1
        
        res = [int(i) for i in str(int_digits)]
        
        return res
        
        
        
