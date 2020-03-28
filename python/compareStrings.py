from collections import Counter
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        word_count = []
        ans = []
        chars ='abcdefghijklmnopqrstuvwxyz'
        for word in words:
            res = Counter(word)
            for ch in chars:
                if ch in res.keys():
                    word_count.append(res[ch])
                    break
        word_count.sort()
        for query in queries:
            res = Counter(query)
            for ch in chars:
                if ch in res.keys():
                    p = res[ch]
                    counter = 0
                    for i in range(len(word_count)-1, -1, -1):
                        if word_count[i]>p:
                            counter +=1
                    ans.append(counter)
                    break
        return ans