class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        remainstr =[]
        finalword = []
        self.word1 = list(word1)
        self.word2 = list(word2)

        def merge(x):
            count = 0
            max = len(x)
            while count < max:
                try:
                    finalword.append(word1[count])
                    finalword.append(word2[count])
                    count+=1
                except IndexError:
                    break

            for x in remainstr:
                for y in x:
                    finalword.append(y)

            word = ''.join(finalword)

            return word


        c = len(word1) - len(word2)

        if c<0:
            remainstr.append(word2[-abs(c):])
            return merge(word1)

        if c>0:
            remainstr.append(word1[-abs(c):])
            return merge(word2)

        if c==0:
            return merge(word1)


word1 = "abc"
word2 = "pqrst"

merge = Solution()
print(merge.mergeAlternately(word1,word2))