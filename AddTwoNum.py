# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Helper Functions

def build_linked_list(nums):
    """Build a linked list from a list of integers."""
    dummy = ListNode()
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


def print_linked_list(node):
    """Print linked list in the format: 7 -> 0 -> 8"""
    values = []
    while node:
        values.append(str(node.val))
        node = node.next
    print("Linked List (reversed digits):", " -> ".join(values))


def print_number(node):
    """Print the actual number represented by the reversed list."""
    digits = []
    while node:
        digits.append(str(node.val))
        node = node.next
    actual_number = "".join(digits[::-1])
    print("Actual Number:", actual_number)


# Core Solution (LeetCode style)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


# User Input

nums1 = list(map(int, input("Enter first number digits (space separated): ").split()))
nums2 = list(map(int, input("Enter second number digits (space separated): ").split()))

l1 = build_linked_list(nums1)
l2 = build_linked_list(nums2)

sol = Solution()
result = sol.addTwoNumbers(l1, l2)

# Output

print_linked_list(result)
print_number(result)