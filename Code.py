class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        l=[]
        for x in sentences:
            l.append(len(x.split(' ')))
        return max(l)
