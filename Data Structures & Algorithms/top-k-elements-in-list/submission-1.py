class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = [[] for i in range(len(nums) + 1)]
        freq_map = defaultdict(int)

        for n in nums:
            freq_map[n] += 1

        for key in freq_map:
            frequencies[freq_map[key]].append(key)

        res = []

        for i in range(len(nums), 0, -1):
            for n in frequencies[i]:
                res.append(n)
                if len(res) == k:
                    return res        
