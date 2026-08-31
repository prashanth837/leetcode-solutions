# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        temp=head.next
        prev=head
        a=[]
        node=2
        while temp.next:
            if (temp.val < prev.val and temp.val <temp.next.val) or (temp.val > prev.val and temp.val > temp.next.val):
                a.append(node)
            temp=temp.next
            prev=prev.next
            node+=1
        a.sort()
        min_diff=float('inf')
        for i in range(0,len(a)-1):
            min_diff=min(min_diff,a[i+1]-a[i])
        print(a)
        return [min_diff,a[-1]-a[0]] if len(a)>=2 else [-1,-1]
            