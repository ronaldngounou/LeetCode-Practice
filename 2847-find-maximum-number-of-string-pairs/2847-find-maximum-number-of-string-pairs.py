class Solution(object):
    def maximumNumberOfStringPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for i in range(0, len(words) - 1):
            for j in range(i+1, len(words)):
                rev = "".join(reversed(words[j]))
                if (words[i] == rev):
                    count += 1
        return count
                