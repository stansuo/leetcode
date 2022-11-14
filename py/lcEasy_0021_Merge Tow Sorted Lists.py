# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        return sorted(l1 + l2)



# 詳解: https://ithelp.ithome.com.tw/articles/10213265
# method 1
# from app
# Whilst there are nodes in both lists, link to lowest head node and increment that list.
# Finally link to the list with remaining nodes.
# Time - O(m+n)
# Space - O(1)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):

        prev = dummy = ListNode(None)

        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next
        prev.next = l1 or l2
        return dummy.next


list1 = [1,2,4]
list2 = [1,3,4]
l1 = ListNode(list1[0])
l2 = ListNode(list2[0])

sol = Solution()
print(sol.mergeTwoLists(l1, l2))



# # method 2
# # https://github.com/qiyuangong/leetcode/blob/master/python/021_Merge_Two_Sorted_Lists.py

# class Solution(object):
#     def mergeTwoLists(self, l1, l2):
#         # dummy head
#         pos = dummyHead = ListNode(-1)
#         while l1 is not None and l2 is not None:
#             if l1.val <= l2.val:
#                 pos.next = l1
#                 l1 = l1.next
#             else:
#                 pos.next = l2
#                 l2 = l2.next
#             pos = pos.next
#         # merge residual l1
#         if l1 is not None:
#             pos.next = l1
#         # merge residual l2
#         if l2 is not None:
#             pos.next = l2
#         return dummyHead.next

# # method 3
# # https://github.com/cnkyrpsgl/leetcode/blob/master/solutions/python3/21.py
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         if not l1: return l2
#         elif not l2: return l1
#         if l1.val < l2.val:
#             l1.next = self.mergeTwoLists(l1.next, l2)
#             return l1
#         else:
#             l2.next = self.mergeTwoLists(l1, l2.next)
#             return l2