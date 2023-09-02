import queue
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        # iterate from the end 
        # pop element 
        # check if the popped element is #
        #   if it is # -> we pop the element after it 
        #   else we continue 
        # push elements in a stack
        # At the end we return true if the two elements in the stack are equal
        
        for i in range(len(s)):
            if s[i] == "#":
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(s[i])
        

        for i in range(len(t)):
            if t[i] == "#":
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(t[i])
        
        return s_stack == t_stack
        