class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1freq={}
        winfreq={}
        
        for i in range(len(s1)):
            s1freq[s1[i]] = s1freq.get(s1[i], 0) + 1

            winfreq[s2[i]] = winfreq.get(s2[i], 0) + 1
        
        if s1freq == winfreq:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            winfreq[s2[r]] = winfreq.get(s2[r],0) + 1
            winfreq[s2[l]] -= 1

            if winfreq[s2[l]] == 0:
                del winfreq[s2[l]]
            
            l += 1
            if s1freq == winfreq:
                return True
            
        return False
                

        