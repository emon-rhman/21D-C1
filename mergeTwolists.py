from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2
        return dummy.next


# -------- VS / VS Code Test --------
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


if __name__ == "__main__":
    # list1: 1 -> 2 -> 4
    l1 = ListNode(1, ListNode(2, ListNode(4)))

    # list2: 1 -> 3 -> 4
    l2 = ListNode(1, ListNode(3, ListNode(4)))

    sol = Solution()
    merged = sol.mergeTwoLists(l1, l2)

    print_list(merged)
