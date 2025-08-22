#344. Reverse String
#Write a function that reverses a string. The input string is given as an array of characters s.

class Solution(object):
    def reverseString(self, s):
        l=0
        r=len(s)-1
        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
