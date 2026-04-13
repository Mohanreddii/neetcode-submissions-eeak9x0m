class Solution:
    def minWindow(self, s: str, t: str) -> str:
            
        freq_win = {}
        left = 0
        min_len = float("inf")
        formed = 0
        winl = 0
        winr = 0
        for c in t:
            freq_win[c] = freq_win.get(c,0)+1
        total = len(freq_win)
        for right in range(len(s)):
            char = s[right]
            if char in freq_win:
                freq_win[char] -=1
                if freq_win[char] == 0:
                    formed +=1
            while formed == total and left<=right:
                char = s[left]
                if min_len > right-left+1:
                    min_len = right-left+1
                    winl = left
                    winr = right+1

                if char in freq_win:
                    if freq_win[char]==0:
                        formed -=1
                    freq_win[char] +=1
                left+=1
        return (s[winl:winr] if min_len != float("inf") else "")