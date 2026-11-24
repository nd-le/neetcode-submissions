class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            char_freq = [0] * 26

            for c in word:
                char_freq[ord(c) - ord('a')] += 1

            res[tuple(char_freq)].append(word)

        return res.values()