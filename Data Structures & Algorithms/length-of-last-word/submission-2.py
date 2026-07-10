class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        num = s.split()
        lastword = num[-1]
        return len(lastword)
