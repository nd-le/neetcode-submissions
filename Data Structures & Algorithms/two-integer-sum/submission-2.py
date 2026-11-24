class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #map that stores the list 
        #have a for loop that does through the list 
        # difference = target - curr index of list in the loop
        num_map = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in num_map:
                return [num_map[comp], i]
            num_map[num] = i