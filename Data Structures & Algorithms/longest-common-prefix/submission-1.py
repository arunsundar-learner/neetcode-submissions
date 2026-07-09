class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or not strs[0]:
            return ""
        final=""
        for i in range(len(strs[0])):
            char_01=strs[0][i]
            for j in range(len(strs)):
                if i >= len(strs[j]) or strs[j][i] != char_01:
                    return final
            final += char_01
        return final