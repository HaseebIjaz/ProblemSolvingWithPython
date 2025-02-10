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