class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charFreq = {}
        ans = 0
        l = 0

        for r in range(len(s)):
            charFreq[s[r]] = 1 + charFreq.get(s[r], 0)

            maxFreq = max(charFreq.values())

            while (r - l + 1) - maxFreq > k:
                charFreq[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans