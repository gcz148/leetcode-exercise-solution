class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        pay attention to the near words
        """
        if not A:
            return 0
        if len(A) < 3:
            return 0
        addend = 0
        count = 0
        for i in range(2,len(A)):
            if A[i - 1] - A[i] == A[i - 2] - A[i - 1]:
                addend += 1
                count += addend
            else:
                addend = 0

        return count
