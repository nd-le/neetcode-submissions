class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #need to return the product of whole array besides the current index 
        #can we use a hash map? to store all the values first? 
        #so we need to loop through the whole list so
        res = [1] *(len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
