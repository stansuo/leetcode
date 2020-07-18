# My Solution
class Solution:
    def romanToInt(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        value_dict = {'I':1, 'V':5 , 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000, 'IV': -2, 'IX':-2, 'XL':-20, 'XC':-20, 'CD':-200, 'CM':-200}
        for roman in ['I', 'V', 'X', 'L', 'C', 'D', 'M', 'IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
            sum = sum + (s.count(roman) * value_dict[roman])
        return(sum)

# # Alternative Solution 1
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         """
#         :type s: str
#         :rtype: int
#         """
#         doubles = {'IV': 4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
#         singles = {'I':1, 'V':5 , 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}
        
#         sum = 0
#         i = 0
#         while i < len(s):
#             if i < len(s)-1 and s[i:i+2] in doubles:
#                 sum += doubles[s[i:i+2]]
#                 i += 2
#             else:
#                 sum += singles[s[i]]
#                 i += 1
#         return(sum)

class testSolution:
    input = "IX"
    sol = Solution()
    integer = sol.romanToInt(input)
    print(integer)