class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head):
        """
        Uses an array to find the middle of a linked list
        IF there are 2 middle values, return the second one
        :param head:            [1, 2, 3, 4, 5]
        :return:                [3, 4, 5]
        """
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]

    def middleNode2(self, head):
        """
        Can also use the tortoise and hare pointers
        :param head: ListNode(head)         [1, 2, 3, 4, 5, 6]
        :return:                            [4, 5, 6]
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
