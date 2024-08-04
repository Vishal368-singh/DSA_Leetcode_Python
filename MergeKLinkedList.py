# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        li = []
        for i in lists:
            head = i
            while(head):
                li.append(head.val)
                head  = head.next
        li.sort()
        if len(li)==0:
            return None
        dummy = ListNode(li[0])
        head = dummy
        for i in li[1:]:
            newNode = ListNode(i)
            dummy.next = newNode
            dummy = dummy.next
        return head
            
        