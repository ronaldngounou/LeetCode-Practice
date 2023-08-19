class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        good = 0
        
        for i in range(len(arr) - 2):
            for j in range(i+1, len(arr) - 1):
                for k in range (j+1, len(arr)):
                    if (abs(arr[i] - arr[j]) <= a) and \
                    ( abs(arr[j] - arr[k]) <= b) and \
                    (abs(arr[i] - arr[k]) <= c):
                        good += 1
        
        return good

                


