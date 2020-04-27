class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        dp = []
        dp.append("1") # initial string
        for i in range(1, n):
            lenLast = len(dp[i-1])
            cur = ""
            j = 0
            while j < lenLast:
                k = j
                while k < lenLast - 1 and dp[i-1][k] == dp[i-1][k+1]: # count identical consecutive char
                    k += 1
                cur += str(k-j+1) # append letter times
                cur += dp[i-1][j] # append letter itself
                j = k + 1
            dp.append(cur)
        print(dp)
        return dp[n-1]
    countAndSay(1,5)
    countAndSay(2,7)
    countAndSay(3,12)