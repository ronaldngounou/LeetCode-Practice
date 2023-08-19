class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        res = 0
        for word in words:
            temp = set()
            for w in word:
                temp.add(w)
            for w in temp:
                if w not in allowed:
                    break
            else:
                res += 1
        return res    