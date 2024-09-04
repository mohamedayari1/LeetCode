from itertools import chain
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_anagram(t):

            t_count = {}

            for i in range(len(t)):
                t_count[t[i]] = 1 + t_count.get(t[i], 0)
            return t_count 
        

        freq_map = collections.defaultdict(list)
        for word in strs: 
            anagram = get_anagram(word)
            key = tuple(sorted(anagram.items()))
            freq_map[key].append(word)
        
        result = []
        for l in freq_map.values():
            result.append(l)
        return result