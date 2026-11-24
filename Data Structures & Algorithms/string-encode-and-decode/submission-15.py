class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for word in strs:
            encoded_str += str(len(word)) + "#" + word

        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            len_word = int(s[i:j])
            i = j + 1
            j = i + len_word

            res.append(s[i:j])
            i = j

        return res
