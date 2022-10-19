class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        freq = [[] for i in range (len(words))]
        
        for word in words:
            count[word] = count.get(word,0) + 1
        for word, val in count.items():
            freq[val].append(word)
        
        res = []
        for i in range(len(words) - 1,0,-1):
            freq[i].sort()
            for word in freq[i]:
                res.append(word)
                if len(res) == k:
                    return res
