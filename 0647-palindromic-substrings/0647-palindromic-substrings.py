class Solution:
    def countSubstrings(self, s: str) -> int:
        def helper(left, right):
            result = 0
            while left >=0 and right<len(s) and s[left] == s[right]:
                left -= 1
                right += 1

                result += 1
            return result 
        result = 0 
        #odds
        for i in range(len(s)):
            result += helper(i, i)
        #evens
        for i in range(len(s)-1):
            result += helper(i, i+1)
        
        return result
