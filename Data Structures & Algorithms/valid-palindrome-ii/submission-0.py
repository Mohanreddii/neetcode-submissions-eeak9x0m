class Solution:
    def validPalindrome(self, s: str) -> bool:
        left,right = 0, len(s)-1
        while left <= right:
            if s[left]!=s[right]:
                s_l = s[left+1:right+1]
                s_r = s[left:right]
                return s_l == s_l[::-1] or s_r == s_r[::-1]
            left +=1 
            right -=1
        return True
        