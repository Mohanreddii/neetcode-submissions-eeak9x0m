class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_freq = {}
        for i in range(len(s1)):
            s1_freq[s1[i]] = s1_freq.get(s1[i],0)+1

        left = 0
        win_len = len(s1)
        s2_freq = {}
        for right in range(len(s2)):

            s2_freq[s2[right]] = s2_freq.get(s2[right],0)+1

            if right-left+1 == win_len:
                if s2_freq == s1_freq:
                   return True
                   
                s2_freq[s2[left]] -=1
                if s2_freq[s2[left]] == 0:
                    del s2_freq[s2[left]]
                
                left+=1
        return False
        