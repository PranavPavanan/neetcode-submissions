class Solution:
    def isPalindrome(self, s: str) -> bool:
        strin=""
        for c in s:
            if c.isalnum():
                strin += c.lower()
        if strin == strin[::-1]:
            return True
        return False
