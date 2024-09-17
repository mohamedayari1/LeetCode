class Solution:
    def get_anagram(self,s: str) -> frozenset[str]:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        anagram = frozenset(freq.items())


        return anagram

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = collections.defaultdict(list)
        for s in strs:
            anagrams_map[self.get_anagram(s)].append(s)
        return list(anagrams_map.values())