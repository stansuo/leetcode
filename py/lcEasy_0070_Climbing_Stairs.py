class Solution:
    def climbStairs(self, n: int) -> int:
        def adder(self, steps_taken: list, n: int) -> list:
            for step_type in {1, 2}:
                next_steps_taken = steps_taken.copy()
                next_steps_taken.append(step_type)
                total_stairs = sum(next_steps_taken)
                if total_stairs < n:
                    adder(self, next_steps_taken, n)
                elif total_stairs == n:
                    options.append(next_steps_taken)
                    break
                elif total_stairs > n:
                    break
        steps_taken = []
        options = []
        adder(self, steps_taken, n)
        return len(options)