class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        first, f(2*k+1)=f(2*k)
        second, f(2*k)=2*k-2*f(k)+2
        third, f(2^(2*k))=(2^(2*k)+2)/3
        four, f(2^(2*k+1))=(2*2^(2*k+1)+2)/3
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n % 2:
            n -= 1
        if (n-1) & n == 0:
            index = 0
            tempN = n
            tempN = tempN >> 1
            while tempN > 0:
                index += 1
                tempN = tempN >> 1

            ans = 0
            if index % 2:
                  tempN = n << 1
            else:
                tempN = n
            ans = (tempN + 2) // 3
            return ans
        else:
            tempAns = self.lastRemaining( n >> 1)
            ans = n - 2 * tempAns + 2
            return ans
