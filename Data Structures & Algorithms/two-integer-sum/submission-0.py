class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        n_map = {}

        for i in range(len(nums)):
            n = nums[i]
            diff = target - n
            if diff in n_map:
                return [n_map[diff], i]
            n_map[n] = i