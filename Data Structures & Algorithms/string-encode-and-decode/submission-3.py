class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        s = ""
        for string in strs:
            s += str(len(string))
            s += '#'
            s += string
        return s

    def decode(self, s: str) -> List[str]:
        l = []
        if s == "":
            return []
        j = 0
        current_index = 0
        while j < len(s):
            while s[j] != '#':
                j += 1
            slen = int(s[current_index:j])
            current_index = j + 1
            l.append(s[current_index:(current_index + slen)])
            j = current_index + slen
            current_index = j
        return l
