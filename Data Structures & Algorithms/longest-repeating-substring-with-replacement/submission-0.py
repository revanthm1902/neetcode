class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c={}
        maxFreq,maxLen=0,0
        l=0
        for r in range(len(s)):
            c[s[r]]=c.get(s[r],0)+1
            maxFreq=max(maxFreq,c[s[r]])

            while (r-l+1)-maxFreq>k:
                c[s[l]]-=1
                l+=1
            maxLen=max(maxLen,r-l+1)
        return maxLen