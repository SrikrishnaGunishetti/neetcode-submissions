class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d.keys():   d[i]=1
            else:   d[i]+=1
        lon=[]
        for i in range(k):
            hestk=next(iter(d))
            for j in d:
                if d[j]>d[hestk]:   hestk=j
            lon.append(hestk)
            del d[hestk]
        return lon