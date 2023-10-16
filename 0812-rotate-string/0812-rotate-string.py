class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        doubled_s = s + s
        
        if goal in doubled_s:
            return True 
        return False
        