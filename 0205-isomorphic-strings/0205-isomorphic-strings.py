class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        freq={}
        for i in range(len(s)):
            if s[i] not in freq:
                if t[i] in freq.values():
                    return False
                else:
                    freq[s[i]]=t[i]
            else:
                if freq[s[i]]!=t[i]:
                    return False
        return True
        