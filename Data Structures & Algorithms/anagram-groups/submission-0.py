class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # map character count to list of anagrams with that character count
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(word)

        return res.values()
