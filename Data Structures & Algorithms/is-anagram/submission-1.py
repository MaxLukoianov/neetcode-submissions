class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        S = defaultdict(int)
        T = defaultdict(int)

        for i in range(len(s)):
            S[s[i]] += 1
            T[t[i]] += 1
        return S == T