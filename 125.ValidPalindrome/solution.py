class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.split(" "))
        n = len(s)
        for i in range(n//2):
            print(i)
            print(n)
            if s[i] != s[n-1-i]:
                return False
        return True