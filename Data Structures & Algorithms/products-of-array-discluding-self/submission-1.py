class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[1]*len(nums)
        a=0
        pref=1
        postf=1
        for i in range(len(nums)):
            l[i]*=pref
            pref*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            l[i]*=postf
            postf*=nums[i]
        return l
        
        
        
'''
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
        '''