from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup_index=[]
        for i in range(1, len(nums)):
            if nums[i] == nums[i -1]:
                dup_index.append(i)
        for j in range(-1, -len(dup_index)-1, -1):
            del nums[dup_index[j]]
        return len(nums)

# class testSolution:

print("Start testing...")
try:
    ex1 = Solution()
    nums = [1,1,2]
    out1 = ex1.removeDuplicates(nums)
    assert out1 == 2 

    ex2 = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    out2 = ex2.removeDuplicates(nums)
    assert out2 == 5  

    ex3 = Solution()
    nums = [1]
    out3 = ex3.removeDuplicates(nums)
    assert out3 == 1
except:
    print("Exception occurred")
    raise
else:
    print("Test complete, no issues found")
finally:
    print("This is the finally block")


