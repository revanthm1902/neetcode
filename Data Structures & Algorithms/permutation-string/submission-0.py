class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2=len(s1),len(s2)
        if n1>n2:
            return False
        s1_cnt=Counter(s1)
        win_cnt=Counter(s2[:n1])
        if s1_cnt==win_cnt:
            return True
        for i in range(n1,n2):
            win_cnt[s2[i]]+=1
            l=s2[i-n1]
            win_cnt[l]-=1
            if win_cnt[l]==0:
                del win_cnt[l]
            if s1_cnt==win_cnt:
                return True
        return False