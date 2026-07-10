class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = ""

        for ch in s:
            if ch.isalnum():
                c += ch.lower()

        return c == c[::-1]