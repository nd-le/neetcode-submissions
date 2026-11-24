class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        pre = 1

        for n in nums:
            answer.append(pre)
            pre *= n 

        post = 1

        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= post
            post *= nums[i]

        return answer