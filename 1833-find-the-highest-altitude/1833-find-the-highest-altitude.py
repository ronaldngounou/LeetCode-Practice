class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        res = [0]
        idx = 0
        for i in range (len(gain)):
            res.append(res[idx] + gain[i])
            idx += 1
        return max(res)
