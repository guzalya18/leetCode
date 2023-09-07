class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""
        for elem in address:
            if elem == ".":
                result += "[.]"
            else:
                result += elem
        return result

