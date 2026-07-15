class Solution(object):
    def isPalindrome(self, s):

        # c = ""

        # for ch in s:
        #     if ch.isalnum():
        #         c = c + ch.lower()
                
        # return c[:] == c[::-1]
       
      






        c = ""

        for ch in s:
            if ch.isalnum():
                c = c + ch.lower()
        return c == c[::-1]