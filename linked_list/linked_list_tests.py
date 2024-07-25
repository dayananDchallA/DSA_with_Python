class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedListTest:
    @staticmethod
    def create_linked_list(vals):
        head = ListNode(vals[0])
        current = head
        for val in vals[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    @staticmethod
    def print_linked_list(head):
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

    def test_reverse_list(self):
        print("Testing Reverse Linked List:")
        head = self.create_linked_list([1, 2, 3, 4, 5])
        self.print_linked_list(head)
        solution = Solution()
        reversed_head = solution.reverseList(head)
        self.print_linked_list(reversed_head)

    def test_merge_two_lists(self):
        print("Testing Merge Two Sorted Lists:")
        l1 = self.create_linked_list([1, 2, 4])
        l2 = self.create_linked_list([1, 3, 4])
        self.print_linked_list(l1)
        self.print_linked_list(l2)
        solution = Solution()
        merged_head = solution.mergeTwoLists(l1, l2)
        self.print_linked_list(merged_head)

    def test_remove_nth_from_end(self):
        print("Testing Remove Nth Node From End of List:")
        head = self.create_linked_list([1, 2, 3, 4, 5])
        self.print_linked_list(head)
        solution = Solution()
        updated_head = solution.removeNthFromEnd(head, 2)
        self.print_linked_list(updated_head)

    def test_has_cycle(self):
        print("Testing Cycle Detection in Linked List:")
        head = self.create_linked_list([3, 2, 0, -4])
        head.next.next.next.next = head.next  # Create a cycle
        solution = Solution()
        has_cycle = solution.hasCycle(head)
        print(f"Has cycle: {has_cycle}")

    def test_is_palindrome(self):
        print("Testing Palindrome Linked List:")
        head = self.create_linked_list([1, 2, 2, 1])
        self.print_linked_list(head)
        solution = Solution()
        is_palindrome = solution.isPalindrome(head)
        print(f"Is palindrome: {is_palindrome}")

    def test_add_two_numbers(self):
        print("Testing Add Two Numbers:")
        l1 = self.create_linked_list([2, 4, 3])
        l2 = self.create_linked_list([5, 6, 4])
        self.print_linked_list(l1)
        self.print_linked_list(l2)
        solution = Solution()
        added_head = solution.addTwoNumbers(l1, l2)
        self.print_linked_list(added_head)

# Define the Solution class with all required methods
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        else:
            tail.next = l2

        return dummy.next

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next

    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)

            current.next = ListNode(out)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

# Instantiate and run tests
if __name__ == "__main__":
    tester = LinkedListTest()
    tester.test_reverse_list()
    tester.test_merge_two_lists()
    tester.test_remove_nth_from_end()
    tester.test_has_cycle()
    tester.test_is_palindrome()
    tester.test_add_two_numbers()
