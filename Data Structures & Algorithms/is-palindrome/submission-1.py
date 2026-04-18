class Solution:
    def isPalindrome(self, s: str) -> bool:
       rev_s = ''
       for char in s:
        if char.isalnum():
            rev_s = rev_s+char.lower()
       return rev_s == rev_s[::-1]

        