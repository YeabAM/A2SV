class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}
        
        def dp(i, total):
            if (i, total) in memo:
                return memo[(i, total)]
            if i == len(nums):
                if total == 0:
                    return 1
                else:
                    return 0
            
            memo [(i, total)] = dp(i+1, total - nums[i]) + dp(i+1, total + nums[i])
            
            return memo[(i, total)]
        
        return dp(0, target)
        