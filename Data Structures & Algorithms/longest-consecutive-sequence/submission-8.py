class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mc=0
        l=set(nums)
        for i in l:
            sc=1
            while i+sc in l:
                sc+=1
            mc=max(mc,sc)
        return mc
