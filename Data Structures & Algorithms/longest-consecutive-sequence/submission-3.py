class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mc=0
        l=list(set(nums))
        for i in l:
            sc=1
            while i-1 in l:
                sc+=1
                i-=1
            mc=max(mc,sc)
        return mc
