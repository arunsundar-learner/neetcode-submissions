class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs[0])      # Start with the length of the first string
        prefix = strs[0]           # Assume the whole first string is the prefix

        for s in strs:             # Check each string in the list
            while s[0:length] != prefix[0:length]:
                length -= 1        # Shrink the prefix length until it matches
        return prefix[0:length]    # Return the common prefix
