class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        list_int = list(str(x)) 
        list_int.reverse()
        #print(list_int)
        if(list_int[-1] == '-'):
            removed_elem = list_int.pop(-1)
            list_int.insert(0, removed_elem)
            
        x = int("".join(list_int))
        #print("rev", rev)
    
        if (x > 2**31 or x < -2**31-1):
            return 0
        else:
            return x
        
        