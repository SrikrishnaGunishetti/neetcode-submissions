class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        i=0
        while i<len(nums):
            product=1
            for j in range(len(nums)):
                if i!=j:
                    product*=nums[j]
            l.append(product)
            i+=1
        return l