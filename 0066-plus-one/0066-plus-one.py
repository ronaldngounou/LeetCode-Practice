class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #can we google a way to convert list to int during the interview?
        
        strs = [str(digit) for digit in digits]
        str_digits = "".join(strs)
        
        int_digits = int(str_digits)
        int_digits += 1
        
        res = [int(i) for i in str(int_digits)]
        
        return res
        
        
        