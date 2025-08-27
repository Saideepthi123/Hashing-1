# // Time Complexity : O(n)
# // Space Complexity : O(n) 
# // Did this code successfully run on Leetcode : yes
# // Any problem you faced while coding this : No
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        # change letter in. pattern with the word in s and keep track of what letter is changed to what word
        # for example in first case we changed a to dog and later we want to change the a again to cat that means 
        # it breaks the pattern and we can return false

        # null and empty check
        if(s is None or len(s) == 0):
            return False

        # split s str with " " space as the delimeter and iterate towards them 
        s_list = s.split(" ") # sc O(n)

        # pattern and s maps to keep track of what letter is changed to which word and vice versa
        pattern_map = {} # to check the condition that each letter maps one unique word in s , sc O(n)
        s_map = {} # to check each unique word is mapped to exactly one letter in pattern, sc O(n)

        if len(s_list) != len(pattern):
            return False

        for i in range(len(pattern)): # tc:O(n)
            pattern_char = pattern[i] # iterating the letter in that index
            s_char = s_list[i] # iterating thr word at that index

            if pattern_char in pattern_map: # if the letter is already mapped in that dic
                if pattern_map[pattern_char] != s_char: # and if the letter is not mapped to the word in s found breach
                    return False # return false
            else:
                pattern_map[pattern_char] = s_char # if the letter is not mapped yet, map it with the word in the s

            
            if s_char in s_map:
                if s_map[s_char] != pattern_char:
                    return False
            else:
                s_map[s_char] = pattern_char

        
        return True


