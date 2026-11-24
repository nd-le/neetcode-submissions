class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while numbers[l] + numbers[r] != target:
            n = numbers[l] + numbers[r]
            while l < r and n > target:
                r -= 1
                n = numbers[l] + numbers[r]

            while l < r and n < target:
                l += 1
                n = numbers[l] + numbers[r]

        return [l + 1, r + 1]
            