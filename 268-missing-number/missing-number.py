class Solution:
    def missingNumber(self, nums: List[int]) -> int:
 
        sum_nums = sum(nums)
    
        sum_n = sum(range(0,len(nums)+1))
            
        ans = sum_n - sum_nums
        
        return ans

        

        