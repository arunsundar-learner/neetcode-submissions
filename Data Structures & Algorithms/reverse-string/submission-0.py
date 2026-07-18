class Solution:
     def reverseString(self, s: List[str]) -> None:
        v=[None]*len(s)
        k = len(s) - 1
        for i in range(len(s)):
            v[k]=s[i]
            k-=1
        s[:]=v
        return s


        