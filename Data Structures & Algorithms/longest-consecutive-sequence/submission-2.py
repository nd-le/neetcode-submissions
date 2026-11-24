class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSeq = 0

        for n in numSet:
            lastNumInSeq = n
            seqLen = 1
            while lastNumInSeq + 1 in numSet:
                seqLen += 1
                lastNumInSeq += 1
            
            longestSeq = max(longestSeq, seqLen)

        return longestSeq