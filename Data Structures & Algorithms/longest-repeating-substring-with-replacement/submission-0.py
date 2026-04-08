class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        left = 0
        freq_dict = {}
        for right in range(len(s)):
            if s[right]  not in freq_dict:
                freq_dict[s[right]] = 1
            else:
                freq_dict[s[right]] += 1
            w_len = right -left + 1
            
            while (right-left+1) - max(freq_dict.values()) > k:

                freq_dict[s[left]] -= 1
                left  += 1

            max_len = max(max_len,right-left+1)
        return max_len