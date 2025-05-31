#9. Palindrome Number
#Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)  # Convert the number to a string
        return x_str == x_str[::-1]  # Compare the string with its reverse
