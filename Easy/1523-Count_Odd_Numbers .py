# 1523. Count Odd Numbers in an Interval Range
# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = (high - low) // 2
        if low % 2 == 1 or high % 2 == 1:
            count += 1
        return count
