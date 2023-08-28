class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        s = []
        while(i >= 0 or j >= 0 or carry == 1):
            sum = carry
            if (i >= 0):
                carry += int(a[i])
                i -= 1
            if (j >= 0):
                carry += int(b[j])
                j -= 1
            s.append(str(carry % 2))
            carry //= 2
            
        return ''.join(reversed(s))
            
                