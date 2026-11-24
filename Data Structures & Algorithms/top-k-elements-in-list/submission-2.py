class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        res = []
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for num, count in count.items():
            buckets[count].append(num)

        for i in range(len(buckets) - 1, -1, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
