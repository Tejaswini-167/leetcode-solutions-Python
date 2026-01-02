# 2520. Count the Digits That Divide a Number

# Given an integer num, return the number of digits in num that divide num.
# An integer val divides nums if nums % val == 0.

class Solution:
    def countDigits(self, num: int) -> int:
        temp=num
        count=0
        while temp>0:
            r=temp%10
            if num%r == 0:
                count+=1
            temp//=10
        return count
 