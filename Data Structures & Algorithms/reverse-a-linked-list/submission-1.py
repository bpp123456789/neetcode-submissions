# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return None

        newHead = ListNode()
        newHead.val = None

        while head.next != None:
            if newHead.val != None:
                newNode = ListNode(head.val, newHead)
                newHead = newNode
            else:
                newHead.val = head.val
            head = head.next
        if newHead.val != None:
            newNode = ListNode(head.val, newHead)
            newHead = newNode
        else:
            newHead.val = head.val
        return newHead

            
        