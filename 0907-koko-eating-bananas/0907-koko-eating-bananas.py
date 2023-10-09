class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while (low <= high):
            mid = (low+high)//2
            reqTime = self.calculateHours(piles, mid)
            if reqTime <= h:
                ans = mid 
                high = mid - 1  
            else:
                low = mid + 1 
        return low 


    def calculateHours(self, piles, hourly):
        totalHours = 0
        for i in range(len(piles)):
            totalHours += math.ceil(piles[i]/hourly)
        return totalHours
    
    # TC: O(n * max(piles)): a brute for approach would consist of iterating until the max element in the piles array. We can reduce the time complexity by using a binary search approach and eliminate the half we are sure the minimum will not be inside. 
    # TC: O(N * log(max(piles))) where N = size of the array and max(piles) is the maximum elmeent in the array