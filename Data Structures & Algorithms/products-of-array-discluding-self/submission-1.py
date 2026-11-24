class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forwardPass = nums.copy()
        backwardPass = nums.copy()

        pre = 1
        for i in range(len(nums)):
            forwardPass[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(len(nums) - 1, -1, -1):
            backwardPass[i] = post
            post *= nums[i]

        result = [a * b for a, b in zip(forwardPass, backwardPass)]

        return result