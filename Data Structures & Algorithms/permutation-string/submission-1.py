class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        ##fixed sliding window
        ##use a dictionary, if the freq of the letters are the same then it is true

        n = len(s1)
        count1 = {}
        count2 = {}

        for c in s1:
            count1[c] = 1 + count1.get(c,0)
        

        l = 0

        for r in range(len(s2)):
            count2[s2[r]] = 1 + count2.get(s2[r], 0)

            if (r - l + 1) > n:
                count2[s2[l]] -= 1
                if count2[s2[l]] == 0:
                    del count2[s2[l]]
                l += 1
            
            if count1 == count2:
                return True
        

        return False 
            

        