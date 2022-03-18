class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {}
        for i in range(len(s)):
            last_occ[s[i]] = i
        result = ''
        for i, c in enumerate(s):
            if c not in result:
                while c < result[-1:] and i < last_occ[result[-1]]:
                    result = result[:-1]
                result += c
        return result