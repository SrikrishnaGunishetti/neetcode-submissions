class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            key=tuple(sorted(i))
            if key not in d.keys():
                d[key]=[i]
            else:
                d[key].append(i)
        l=[]
        for i in d:
            l.append(d[i])
        return l