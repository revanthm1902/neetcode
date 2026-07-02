class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums.sort()
        # miss=1
        # for num in nums:
        #     if num<=0:
        #         continue
        #     elif num==miss:
        #         miss+=1
        #     elif num>miss:
        #         return miss
        # return miss

        n=len(nums)
        i=0
        while i<n:
            if 1<=nums[i]<=n:
                crct_idx=nums[i]-1
                if nums[i]!=nums[crct_idx]:
                    nums[i],nums[crct_idx]=nums[crct_idx],nums[i]
                else:
                    i+=1
            else:
                i+=1
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1





