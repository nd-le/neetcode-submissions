class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:

            n = str(n)
            digitsSquared = 0

            for c in n:
                digitsSquared += int(c) ** 2

            if digitsSquared in seen:
                return False

            seen.add(digitsSquared)
            n = digitsSquared

        return True