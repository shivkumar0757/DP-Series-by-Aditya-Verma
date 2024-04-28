# link for the problem
# https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1

from functools import lru_cache

class Solution:
    # Recursive Solution
    def mcm_rec(self, N, arr):
        
        def mcm(i, j, arr):
            if i>=j:
                return 0
            res = float('inf')
            for k in range(i, j):
                temp = mcm(i, k, arr) + mcm(k+1, j, arr) + (arr[i-1]*arr[k]*arr[j])
                res = min(temp, res)
            return res
            
        return int(mcm(1,N-1,arr))
    
    # Storing the results
    def mcm_memo(self, N, arr):
        # code here
        dp = [[-1]*(N+1) for _ in range(N+1)]
        def mcm(i, j, arr):
            if i>=j:
                return 0
                
            if dp[i][j] != -1: return dp[i][j]
            res = float('inf')
            
            for k in range(i, j):
                temp = mcm(i, k, arr) + mcm(k+1, j, arr) + (arr[i-1]*arr[k]*arr[j])
                res = min(temp, res)
            dp[i][j] = res
            return res
        return int(mcm(1,N-1,arr))
        
        
    # Using cache from functool library
    def mcm_cache_annotation(self, N, arr):
        @lru_cache(None)
        def mcm(i, j):
            if i>=j: return 0
            
            res = float('inf')
            
            for k in range(i, j):
                temp_res = mcm(i, k) + mcm(k+1, j) + (arr[i-1]  * arr[k] * arr[j])
                res = min(res, temp_res)
            return res
        return mcm(1, N-1)
    
    # Bottom up approach for tabularion
    def mem_tabulation(self, N, arr):
        dp = [[0]*N for _ in range(N)]
        
        # No need to write base case, as 
        # i==j will be 0 and we have initialised the full dp to 0
        
        # fill dp for all length of 2, 3, ... to N-1
        for L in range(2, N):
            for i in range(1, N-L+1): #For each sub prob of length L (fill dp), lets say all of size 2 , i(2- N-L+1)
                j = i + L -1
                dp[i][j] = float('inf')
                for k in range(i,j):
                    q = dp[i][k] + dp[k+1][j] + (arr[i-1]*arr[k]*arr[j])
                    
                    dp[i][j] = min(q, dp[i][j])
        return dp[1][N-1]



            
    


