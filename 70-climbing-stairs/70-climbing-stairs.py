from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        @lru_cache()
        def dp(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            
            return dp(n-1) + dp(n-2)
        
        return dp(n)
        