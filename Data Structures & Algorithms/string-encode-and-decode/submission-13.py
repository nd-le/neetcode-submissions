class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            wordLength = len(word)
            string += str(wordLength) + '#' + word

        return string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            wordLength = ""
            while s[i] != '#':
                wordLength += s[i]
                i += 1
            
            res.append(s[i + 1: i + 1 + int(wordLength)])

            i += 1 + int(wordLength)
        return res
