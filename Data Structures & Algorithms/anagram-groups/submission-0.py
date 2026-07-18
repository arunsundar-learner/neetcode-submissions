class Solution:
       def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}

        for s in strs:
            sorted_s = sorted(s)
            sorted_string = ''.join(sorted_s)
            print(sorted_string)
            if sorted_string not in d:
                d[sorted_string] = [s]
            else:
                d[sorted_string].append(s)

        return list(d.values())
