class Solution:
    def longestCommonPrefix(self, strs: List[str]):

        # strs.sort()

        # first = strs[0]
        # last = strs[-1]

        # i = 0

        # while i < len(first) and i < len(last):

        #     if first[i] != last[i]:
        #         break
        #     i += 1
        # return first[:i]

        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

        return prefix