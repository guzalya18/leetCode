class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(elem.lower() for elem in s if elem.isalnum())
        if s ==s[::-1]:
            return True
        else:
            return False
