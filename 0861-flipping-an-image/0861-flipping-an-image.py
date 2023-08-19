class Solution(object):
    def flip(self, nums):
        for num in nums:
            num = num.reverse()
        

    def invert(self, nums):
        for num in nums:
            for i in range(len(num)):
                if num[i] == 0:
                    num[i] = 1
                elif num[i] == 1:  
                    num[i] = 0
        return nums

    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        
        self.flip(image)
        
        final = self.invert(image)
        
        
        return final 

    