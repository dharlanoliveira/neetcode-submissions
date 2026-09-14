class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)

        if(len(s1) > len(s2)):
            return False

        while(r < len(s2) + 1):
            s_s2 = sorted(s2[l:r])
            s_s1 = sorted(s1)
            if(s_s1 != s_s2):
                l += 1
                r += 1
            else: 
                return True    

        return False