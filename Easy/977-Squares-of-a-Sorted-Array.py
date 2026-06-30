# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_arr = []

        for i in nums:
            i = i * i
            sorted_arr.append(i)

        sorted_arr.sort()

        return sorted_arr


# Driver Code
nums = [-4, -1, 0, 3, 10]

obj = Solution()
print(obj.sortedSquares(nums))
