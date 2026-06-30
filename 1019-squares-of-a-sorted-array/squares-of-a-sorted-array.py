class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_arr =[]
        for i in nums:
            i = i*i
            sorted_arr.append(i)

        sorted_arr.sort()

        return sorted_arr
        

    

