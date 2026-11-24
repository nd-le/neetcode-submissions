class Solution:
    from collections import Counter
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = Counter(nums)
        for val in res.values():
            if val > 1:
                return True
        return False