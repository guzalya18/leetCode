class Solution:
    def longestCommonPrefix(self, S: List[str]) -> str:
        if (len(S) == 0):
            return ""
        for i in range(len(S[0])):
            c = S[0][i]
            for j in range(len(S)):
                if (i == len(S[j]) or S[j][i] != c):
                    return S[0][0:i];
        return S[0]