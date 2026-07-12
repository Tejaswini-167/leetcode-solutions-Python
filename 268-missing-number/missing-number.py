class Solution:
    def missingNumber(self, nums: List[int]) -> int:
 
        # sum_nums = sum(nums)
    
        # sum_total = sum(range(0,len(nums)+1))
            
        # return sum_total - sum_nums

        n = len(nums)

        return (n * (n + 1) // 2) - sum(nums)

        

        