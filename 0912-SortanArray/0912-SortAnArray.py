class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        else:
            middle = len(nums) //2
            #keep on doing it until we have an array of 1
            left_values = self.sortArray(nums[:middle])
            right_values = self.sortArray(nums[middle:])
            left_index = 0
            right_index = 0
            sorted_array = []


            #we implemented first of an array of 2
            while left_index < len(left_values) and right_index < len(right_values):
                if left_values[left_index] < right_values[right_index]:
                    sorted_array.append(left_values[left_index])
                    left_index += 1
                else:
                    sorted_array.append(right_values[right_index])
                    right_index += 1
            sorted_array += right_values[right_index:] # += because we add an array and not a value
            sorted_array += left_values[left_index:]
        
        return sorted_array


        
        



