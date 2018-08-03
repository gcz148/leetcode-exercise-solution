class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        dp[i][dist]=sum(dp[j][dist],{j,0,i-1})
        """
        if not A:
            return 0
        answer,n=0,len(A)
        if n < 3:
            return 0
        dp = [{} for i in range(n)]
        for i in range(1,n):
            for j in range(i):
                distance = A[i] - A[j]
                s = dp[j].get(distance,0) + 1
                dp[i][distance] = dp[i].get(distance,0) + s
                answer += s-1
        return answer
