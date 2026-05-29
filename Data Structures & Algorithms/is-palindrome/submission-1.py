class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = s.lower()
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and s[i] not in chars:
                i += 1
            while j > i and s[j] not in chars:
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
