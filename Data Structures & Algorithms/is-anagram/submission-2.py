class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        e={}
        for i in s:
            if i not in d.keys():   d[i]=1
            else:   d[i]=d[i]+1
        for i in t:
            if i not in e.keys():   e[i]=1
            else:   e[i]=e[i]+1
        return(d==e)