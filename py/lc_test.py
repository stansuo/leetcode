# 20. Valid Parentheses

class Solution:    # V2
    def isValid(self, s: str) -> bool:
        paired = {')': '(', '}': '{', ']': '['}
        # print(paired)
        stack = []
        for letter in s:
            if letter in paired:
                if not stack or stack.pop() != paired[letter]:
                    return False
                    
            else:
                stack.append(letter)

            # print("letter: ", letter)
            # print("stack: ", stack)
            # print("lefty: ", letter in lefty)
            # print("righty: ", letter in righty)
        return not stack

# class Solution:
#     def isValid(self, s: str) -> bool:
#         righty = [')', '}', ']']
#         lefty = ['(', '{', '[']
#         paired = dict(zip(righty, lefty))
#         print(paired)
#         stack = []
#         for letter in s:
#             if letter in paired.values():
#                 stack.append(letter)
#             else:
#                 try: 
#                     if stack.pop() != paired[letter]:
#                         return False
#                 except IndexError as err:
#                     # print("IndexError:", err)
#                     return False        

#             # print("letter: ", letter)
#             # print("stack: ", stack)
#             # print("lefty: ", letter in lefty)
#             # print("righty: ", letter in righty)
        
#         if len(stack) == 0:
#             return True
#         else:
#             return False


# Testing...
test = Solution()

ipt = "()"
opt = test.isValid(ipt)
print('output1',opt)    # true

ipt = "()[]{}"
opt = test.isValid(ipt)
print('output2',opt)    # true

ipt = "(]"
opt = test.isValid(ipt)
print('output3',opt)    # false

ipt = "([)]"
opt = test.isValid(ipt)
print('output4',opt)    # false

ipt = "{[]}"
opt = test.isValid(ipt)
print('output5',opt)    # true

ipt = "]"
opt = test.isValid(ipt)
print('output6',opt)    # false

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true
