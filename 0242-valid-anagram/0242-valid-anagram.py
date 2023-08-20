class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(t) != len(s):
            return False
       
        s_freq = {}
        t_freq = {}

        for ch in s:
            s_freq[ch] = s_freq.get(ch, 0) + 1
        for ch in t:
            t_freq[ch] = t_freq.get(ch, 0) + 1
        
        return s_freq == t_freq
