class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        info="qwertyuiopasdfghjklzxcvbnm1234567890"
        f=0
        l=len(s)-1
        while f<l:
            if s[f] not in info:
                f+=1
            if s[l] not in info:
                l-=1
            if s[f] in info and s[l] in info:
                if s[f]!=s[l]:
                    return False
            f+=1
            l-=1
        return True