#13. Roman to Integer
#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        def char_roman_to_int(c):
            if c == 'I':
                return 1
            elif c == 'V':
                return 5
            elif c == 'X':
                return 10
            elif c == 'L':
                return 50
            elif c == 'C':
                return 100
            elif c == 'D':
                return 500
            elif c == 'M':
                return 1000
            else:
                return 0

        res = 0
        i = 0
        while i < len(s):
            current = char_roman_to_int(s[i])
            next_val = char_roman_to_int(s[i + 1]) if i + 1 < len(s) else 0
            if current < next_val:
                res += (next_val - current)
                i += 2
            else:
                res += current
                i += 1
        return res