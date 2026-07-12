class Solution:
    def firstUniqChar(self, s: str) -> int:
        # d = {}
        # for ch in s:

        #     d[ch] = d.get(ch,0) + 1

        # for i in range(len(s)):

        #     if d[s[i]] == 1:
                
        #         return i
        # return -1

        freq = Counter(s)

        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i
        return -1

       

        
                