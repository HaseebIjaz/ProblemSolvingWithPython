class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # After this line lenghts are equal

## Sorting only makes sense for mutable data structures like list
## It does not make sense for immutable data structires like string
        s.sort()
        t.sort()
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True