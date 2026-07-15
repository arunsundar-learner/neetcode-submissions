class Solution:
     def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word=strs[0]
        length=len(strs[0])
        for i in strs:
            print(i)
            while i[0:length] != first_word[0:length]:
                print("i")
                print(i[0:length])
                print("firstword")
                print(first_word[0:length])
                length-=1

        return first_word[0:length]