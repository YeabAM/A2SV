class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
                
            else:
                result[-1][1] = max(interval[1],result[-1][1])
                
        return result
        
        