# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = "".join(s.split(" "))
#         n = len(s)
#         for i in range(n//2):
#             print(i)
#             print(n)
#             if s[i] != s[n-1-i]:
#                 return False
#         return True

class Solution:
    def isPalindrome(self, s:str) -> bool:
        if len(s) <= 1: return True

        new_s = ''
        for c in s:
            if c.isalnum():
                new_s += c.lower()

        return new_s == new_s[::-1]

class Solution:
    def isAlphaNum(self, c:str) -> bool:
        return (ord('A') <= ord(c) and ord(c) <= ord('Z') or
                ord('a') <= ord(c) and ord(c) <= ord('z') or
                ord('0') <= ord(c) and ord(c) <= ord('9'))

    def isPalindrome(self, s:str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while l < r and not self.isAlphaNum(s[r]):
                r -= 1
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1 