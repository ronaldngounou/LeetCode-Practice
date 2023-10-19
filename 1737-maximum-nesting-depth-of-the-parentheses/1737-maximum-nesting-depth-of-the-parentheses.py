class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = 0
        for i in range (len(s)):
            if s[i] == '(':
                depth += 1
                max_depth = max(max_depth, depth)
                
            elif s[i] == ')':
                depth -= 1
        
        return max_depth
