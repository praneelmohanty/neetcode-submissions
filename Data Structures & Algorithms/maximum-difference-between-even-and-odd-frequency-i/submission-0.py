class Solution:
    def maxDifference(self, s: str) -> int:
        a1, a2, S = 0, 100, set(list(s))
        for i in S:
            if s.count(i) % 2 != 0:
                a1 = max(a1, s.count(i))
            elif s.count(i) % 2 == 0:
                a2 = min(a2, s.count(i))
        return a1 - a2