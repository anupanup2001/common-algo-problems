import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        count = 0
        for node in lists:
            heapq.heappush(minheap, (node.val, count, node))
            count += 1
        
        sentinel = ListNode()
        currNode = sentinel
        while minheap:
            _, _, smallest = heapq.heappop(minheap)
            currNode.next = smallest
            currNode = smallest
            if smallest.next is not None:
                heapq.heappush(minheap, (smallest.next.val, count, smallest.next))
                count += 1
        currNode.next = None
        return sentinel.next
