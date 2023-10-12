class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        for i in range(len(num)-1, -1, -1):
            ascii_value = ord(num[i])
            if ascii_value % 2 == 1:
                return num[0:i+1]
        
        return ""

        