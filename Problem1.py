    # time complexity : O(n*k)
    # space complexity : O(n*k)
    # Did this code successfully run on Leetcode : yes
    # Any problem you faced while coding this : no
class Problem1(object):
    # the trick part is to idenity anagrams to group
    # 1way is to sort the each str and once we sort the anagrams will be same, so we can used this logic to group
    # other is having a hash function whre for each letter a-z (given strs[i] consists of lowercase English letters. )
    # lets assign a prime number such that when we multiole the letters of a sting only the anagrams will return the same value
    # example ate, tea = example a=2, t=3,e=5 then ate = 2*3*5 and tea= 3*5*2 which is equal so this is better than sorting each str 
    # because if we sort and the compare and group the complexity is O(n*klogk) klogk for sorting, whereas this hash functin O(nk)

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_map = {}

        for str in strs: # Tc O(n)
            hash_str = self.hash_function(str) #Tc O(k)

            if hash_str in anagrams_map:
                anagrams_map[hash_str].append(str)
            else:
                anagrams_map[hash_str] = [str]

        return anagrams_map.values()
    
    def hash_function(self,str):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 
            41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

        hash = 1

        for letter in str:
            hash *= primes[ord(letter) - ord('a')]

        return hash