import collections
class Solution(object):
"""
"""
    def lenLongestFibSubseq(self, A):
        if not A:
            return 0
        if len(A) < 3:
            return 0
        maps = {value: index for index, value in enumerate(A)}
        
        longest = collections.defaultdict(lambda: 2)

        answer = 0
        for k, value in enumerate(A):
            for j in range(k):
                i = maps.get(value - A[j], None)
                if i is not None and i < j:
                    longest[j, k] = longest[i, j] + 1
                    candidate = longest[j, k]
                    answer = max(answer, candidate)

        if answer < 3:
            return 0
        else:
            return answer
