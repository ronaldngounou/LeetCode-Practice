class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        L, R = 0, 1
        maxProfit = 0

        while (R < len(prices)):
            if (prices[L] < prices[R]):
                profit = prices[R] - prices[L]
                maxProfit = max(maxProfit, profit)
            else:
                L = R
            R += 1
                
        
        return maxProfit
