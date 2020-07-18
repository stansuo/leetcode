class Solution:
    def longestCommonPrefix(self, strs) -> str:
        '''
        :type strs: List[str]
        :rtype: str
        '''
        prefix = ""
        try:
            shortest_word = min(strs, key=len)
        except:
            shortest_word = ""
        for i in range(len(shortest_word)):
            if len(prefix) != i:
                break
            char = strs[0][i]
            for j in range(len(strs)):
                if char == strs[j][i]:
                    char = strs[j][i]
                else:
                    break
            else:
                prefix = prefix + char
        return prefix



# class testSolution:
ex1 = Solution()
input_strs1 = ["flower","flow","flight"]
out1 = ex1.longestCommonPrefix(input_strs1)
print(out1) 
# "fl"

ex2 = Solution()
input_strs2 = ["dog","racecar","car"]
out2 = ex2.longestCommonPrefix(input_strs2)
print(out2) 
# ""

ex3 = Solution()
input_strs3 = []
out3 = ex2.longestCommonPrefix(input_strs3)
print(out3) 

# ""
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
# All given inputs are in lowercase letters a-z.