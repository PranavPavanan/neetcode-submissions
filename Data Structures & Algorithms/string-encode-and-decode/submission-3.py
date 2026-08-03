class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word))+"$"+word
        return res

    def decode(self, s: str) -> List[str]:
        strs2, i, length = [], 0, 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            length = int(s[i:j])
            strs2.append(s[j+1:j+1+length])
            i = j+1+length
        return strs2

