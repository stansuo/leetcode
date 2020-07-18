class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        :type n: int
        :rtype: int
        '''
        if n <= 0:
            return 0
        if n <= 2:
            return n
        
        (now, prev) = (2, 1)   # Two ways to reach second step, one way to reach first
        for _ in range (3, n + 1):
            (now, prev) = (now + prev, now)
        
        return now