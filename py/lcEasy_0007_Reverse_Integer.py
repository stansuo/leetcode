class Solution:
    def reverse(self, x):
        if x < 0:
            x = str(-x)
            rev_x = x [-1: -(len(x))-1: -1]
            rev_x = -int(rev_x)
        else:
            x = str(x)
            rev_x = x [-1: -(len(x))-1: -1]
            rev_x = int(rev_x)
        
        if (-(2**31)) <= rev_x <= ((2**31)-1):
            return rev_x
        else: 
            return 0