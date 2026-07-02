class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        miss=1
        for num in nums:
            if num<=0:
                continue
            elif num==miss:
                miss+=1
            elif num>miss:
                return miss
        return miss