class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = {}
        t_count = {}

        for c in s:
            s_count[c] = 1 + s_count.get(c, 0)

        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
        
        return t_count == s_count



