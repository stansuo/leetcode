class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        upperLimit = int((c**(1/2))) +1
        for a in range(0, upperLimit):
            # for j in range(0, upperLimit):
            b = (c - a**2)**(1/2)
            if int(b) == b:
                print('Print True')
                return True
        else:
            print('Print False')
            return False

# test Solution:
ex1 = Solution()
input1 = 9999999999999
out1 = ex1.judgeSquareSum(input1)
print(out1) 

ex2 = Solution()
input2 = 3
out2 = ex2.judgeSquareSum(input2)
print(out2) 


ex3 = Solution()
input3 = 1
out3 = ex3.judgeSquareSum(input3)
print(out3) 

ex4 = Solution()
input4 = 0
out4 = ex4.judgeSquareSum(input4)
print(out4) 
# Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a^2 + b^2 = c.

# Example 1:

# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
 

# Example 2:

# Input: 3
# Output: False