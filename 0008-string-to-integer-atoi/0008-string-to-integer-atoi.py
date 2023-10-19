
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        
        if not s:
            return 0

        negative = False 
        res = 0
        start = 1
        
        if s[0] == '-':
            negative = True
            start = 1 
        elif s[0] == '+':
            negative = False
            start = 1
        elif not s[0].isnumeric():
            return 0
        else:
            start = 0

        for i in range(start, len(s)):
            if s[i].isdigit():
                digit = int(s[i])
                res = res * 10 + digit 
                if not negative and res > 2**31 - 1:
                    return 2**31 - 1
                if negative and res > 2**31:
                    return -2**31
            else:
                break
        
        if not negative and (-2**31 <= res <= 2**31-1):
            return res 
        else:
            return -res