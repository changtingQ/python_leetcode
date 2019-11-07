def del_duplicate_element(str_list: str):
    aa = list(str(str_list))
    bb = list(map(int, aa))
    # print(bb)
    ll = []
    for i in bb:
        if i not in ll:
            ll.append(i)
    z = (map(str, ll))
    x = "".join(z)
    return x
    # str_list = map(str, str_list)
    # aa = "".join(str_list)
    # bb = list(aa)
    # print(bb)

result = del_duplicate_element(1112389)
print(result)

# print("************************answer***************************思路1")


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = set()
        pre = ListNode(float('INF'))
        pre.next = head
        ret = pre
        while head:
            if head.val not in s:
                s.add(head.val)
                pre = pre.next
            else:
                pre.next = head.next
            head = head.next
        return ret.next


