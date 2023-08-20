class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(t) != len(s):
            return False
        else:
            s1 = ''.join(sorted(s))
            t1 = ''.join(sorted(t))
            return s1 == t1
