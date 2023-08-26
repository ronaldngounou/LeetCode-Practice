class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        dic_magazine = {}

        #Build a hashmap with the letters in magazine and their occcurences
        # Iterate in randsome and decrement the values in magazine \
        # return true if all the values in magazine are 0
        for ch in magazine:
            if ch in dic_magazine:
                dic_magazine[ch] = dic_magazine.get(ch) + 1
            else:
                 dic_magazine[ch] = 1
        

        for letter in ransomNote:
            if letter in dic_magazine and dic_magazine[letter] > 0:
                dic_magazine[letter] = dic_magazine.get(letter) - 1
            else:
                return False
        
        return True