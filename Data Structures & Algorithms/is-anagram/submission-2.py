class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ns = sorted(s)
        nt = sorted(t)
        if list(ns) == list(nt) and len(s) == len(t):
            return True
        return False
        