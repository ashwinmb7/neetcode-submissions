class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        

        return "".join(res)

        #strs = neet code love you
        #res = 4#neet4#code4#love3#you

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            

            length = int(s[i:j])

            i = j+1
            j = i + length

            res.append(s[i:j])
            i = j
        
        return res