class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome_map = {}

        def helper(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
            
                left -= 1
                right += 1


            curr_s = s[left+1: right]
            palindrome_map[len(curr_s)] = curr_s

        for i in range(len(s)):
            helper(i, i)
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                helper(i, i+1)
        return palindrome_map[max(palindrome_map.keys())] 
