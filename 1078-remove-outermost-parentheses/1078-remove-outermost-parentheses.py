class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        l = []
        for i in range(len(s)):
            if not stack:
                l.append(i)
                stack.append(s[i])
                continue
            elif s[i] =='(' and stack[-1] == ')':
                stack.pop()
                if not stack:
                    l.append(i)
            elif s[i] == ')' and stack[-1] == '(':
                stack.pop()
                if not stack:
                    l.append(i)
            else:
                stack.append(s[i])
        
        res = ""
        
        for i in range(0, len(l), 2):
            res += s[ l[i]+1 : l[i+1] ]

        return res 