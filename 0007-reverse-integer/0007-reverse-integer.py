class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        #list_int = list(str(x)) 
        #list_int.reverse()
        #print(list_int)
        #if(list_int[-1] == '-'):
        #    removed_elem = list_int.pop(-1)
        #    list_int.insert(0, removed_elem)
            
        #rev = int("".join(list_int))
        #print("rev", rev)
        #return rev
    
        #if (x > 2**31 or x < -2**31 -1):
        #    return 0
        #else:
        #    return x
        
        x_str_splt = [i for i in str(x)]
        new_int = [i for i in reversed(x_str_splt)]

        if new_int[-1] == '-':
            new_int.pop()
            new_int.insert(0, '-')

        x = int(''.join(new_int))
        if x > 2 ** 31 or x < -2 ** 31-1:
            return 0
        else: 
            return x