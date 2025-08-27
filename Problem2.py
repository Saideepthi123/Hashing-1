class Problem2(object):
    # time complexity : O(n) 
    # space complexity : 2O(n) -> O(n)
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # so the strings with same length and the order of the letters should also be mainted in both the strings such that 
        # they both are isomorphic to each other 
        # approch using hash map to store the letter and with what the letter is changed to, so next time when the same letter comes we can check that the letter is alredy changed so we found the breach and can return false
        # keeping both the string map and t string map because not only yhr letters changed to s to match the t , we should also consider that t should also be isomorphic to s 
        # using 2 hash maps and checking once found the breah return false if not true. 

        s_map = {}
        t_map = {}

        for i in range(len(s)): # given t.length == s.length # O(n) time 
            s_char = s[i]
            t_char = t[i]

            if s_char in s_map: # O(1) to search the key in the hashmap
                if s_map[s_char] != t_char: # so the letter is already changed to something else which is not equal to t_char
                    return False 
            else:
                s_map[s_char] = t_char

            if t_char in t_map: 
                if t_map[t_char] != s_char: 
                    return False
            else:
                t_map[t_char] = s_char

        return True


            



