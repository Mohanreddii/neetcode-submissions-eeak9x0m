class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]',"",s).lower()
        rev_s = s[::-1]
        if rev_s == s:
            return True
        return False

        