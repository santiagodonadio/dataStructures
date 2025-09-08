from collections import defaultdict
from typing import List

class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        anagram_map = defaultdict(list)
        
        for s in strs:
            
            sorted_s = tuple(sorted(s))
            anagram_map[sorted_s].append(s)
            
        return list(anagram_map.values())

def main():
    strs = ["eat","tea","tan","ate","nat","bat"]
    
    # Creating an instance of the class Solution
    sol = Solution()
    
    result = sol.groupAnagrams(strs)
    
    print(result)
    

main()