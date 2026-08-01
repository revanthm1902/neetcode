class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        cntT=Counter(t)
        win={}
        have,need=0,len(cntT)
        res,res_len=[-1,-1],float('inf')
        l=0
        for r in range(len(s)):
            ch=s[r]
            win[ch]=win.get(ch,0)+1
            if ch in cntT and win[ch]==cntT[ch]:
                have+=1
            while have==need:
                if r-l+1 <res_len:
                    res=[l,r]
                    res_len=r-l+1
                left_ch=s[l]
                win[left_ch]-=1
                if left_ch in t and win[left_ch]<cntT[left_ch]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if res!=float('inf') else ""