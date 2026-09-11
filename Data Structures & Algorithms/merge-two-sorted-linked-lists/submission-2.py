# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        pointer = newHead
        if list1 == None and list2 == None:
            return None

        while (list1 != None or list2 != None):
            if list1 != None and (list2 == None or list1.val < list2.val):
                pointer.val = list1.val
                if list1.next != None:
                    list1 = list1.next
                else:
                    list1 = None
            else:
                if list2 != None:
                    pointer.val = list2.val
                    if list2.next != None:
                        list2 = list2.next
                    else:
                        list2 = None
            if (list1 != None or list2 != None):
                pointer.next = ListNode()
                pointer = pointer.next
        return newHead
        
            
        