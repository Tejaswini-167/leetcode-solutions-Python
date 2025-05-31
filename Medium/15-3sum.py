
#15. 3Sum
#https://leetcode.com/problems/3sum/
#discription:Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result=[]
        n=len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue 
            left =i+1
            right =n-1
            while left<right:
                total=nums[i]+nums[left]+nums[right] 
                if total == 0:
                    result.append([nums[i],nums[left],nums[right]])
                    left +=1
                    right -=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left <right and nums[right]==nums[right +1]:
                        right -=1
                elif total<0:
                    left +=1
                else:
                    right -=1
        return result


                    

                

