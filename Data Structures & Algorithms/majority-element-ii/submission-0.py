class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt=Counter(nums)
        res=[]
        for x in cnt:
            if cnt[x]>len(nums)//3:
                res.append(x)
        return res