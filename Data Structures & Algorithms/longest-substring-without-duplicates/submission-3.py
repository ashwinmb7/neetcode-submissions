class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in my_set:
                my_set.remove(s[l])
                l += 1
            
            my_set.add(s[r])
            res = max(res, r - l + 1)
        

        return res


        ##abcabcbb
        ##set:a windowSize = 1
        ##set: a,b windowSize = 2
        ##set: a,b,c windowSize = 3
        ##set: b,c,a windowSize = 3
        ##set: c,a,b windowSize = 3


