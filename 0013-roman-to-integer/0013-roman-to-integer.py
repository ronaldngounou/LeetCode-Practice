class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        sum = table[s[len(s)-1]]
        for i in range(len(s)-2, -1, -1):
            if table[s[i]] < table[s[i+1]]:
                sum -= table[s[i]]
            else:
                sum += table[s[i]]
        
        return sum 

        