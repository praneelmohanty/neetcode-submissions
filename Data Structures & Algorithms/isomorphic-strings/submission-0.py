class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if t[i] in d:
                if d[t[i]] != s[i]:
                    return False
            else:
                if s[i] in d.values():
                    return False
                d[t[i]] = s[i]
        return True