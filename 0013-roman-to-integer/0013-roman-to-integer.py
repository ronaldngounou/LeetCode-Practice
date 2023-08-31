class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_table = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        } 
        # 01
        # IV 
        idx = len(s) - 1
        sum = 0
        while idx >= 0:
            #if (idx > 1 and hash_table[s[idx]] > hash_table[s[idx-1]]):
            if (idx < len(s) - 1 and hash_table[s[idx]] < hash_table[s[idx+1]]):
                sum -= hash_table[s[idx]]
            else:
                sum += hash_table[s[idx]]
            idx -= 1
        return sum



