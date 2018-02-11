# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        int_gen = itertools.count()
        min_heap = [(node.val, next(int_gen), node) for node in lists if node]
        heapq.heapify(min_heap)
        header_node = ListNode(None)
        curr_node = header_node
        while min_heap:
            _, _,tmp_node = heapq.heappop(min_heap)
            curr_node.next = tmp_node
            curr_node = curr_node.next
            if tmp_node.next:
                heapq.heappush(min_heap, (tmp_node.next.val, next(int_gen), tmp_node.next))
        return header_node.next
