class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        l = []

        # Solve this problem using a stack and a list to keep track of the indexes where the outer most parenthesis are.
        # Remove the corresponding parenthesis from the stack if they match. If they don't match, append the element in the stack.
        # When the stack is empty, we have reached an outer most parenthesis. Store the index of that outer parenthesis inside a list.
        
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