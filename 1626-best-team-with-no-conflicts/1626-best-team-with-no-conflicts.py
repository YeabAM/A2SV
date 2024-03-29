class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = []
        for score, age in zip(scores, ages):
            pairs.append((score, age))
            
        pairs.sort()
        dp = [pairs[i][0] for i in range(len(pairs))]
        
        for i in range(len(pairs)):
            max_score, max_age = pairs[i]
            for j in range(i):
                cur_score, cur_age = pairs[j]
                if max_age >= cur_age:
                    dp[i] = max(dp[i], max_score + dp[j])
        
        return max(dp)