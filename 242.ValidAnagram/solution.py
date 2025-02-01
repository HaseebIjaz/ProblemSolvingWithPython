class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If Lengths are not equal return early, dont sort.
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If Lengths are not equal return early
        if len(s) != len(t):
            return False

        ## Sorting only makes sense for mutable data structures like list
        ## It does not make sense for immutable data structires like string
        
        count_S, count_T = {}, {}

        for i in range(len(s)):
            count_S[s[i]] = 1 + count_S.get(s[i], 0)
            count_T[t[i]] = 1 + count_T.get(t[i], 0)

        return count_S == count_T
    

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If Lengths are not equal return early
        if len(s) != len(t):
            return False

        ## Sorting only makes sense for mutable data structures like list
        ## It does not make sense for immutable data structires like string
        
        count_S, count_T = {}, {}

        for i in range(len(s)):
            count_S[s[i]] = 1 + count_S.get(s[i], 0)
            count_T[t[i]] = 1 + count_T.get(t[i], 0)

        for chr in count_S:
            if count_S[chr] != count_T.get(chr, 0):
                return False

        return True    