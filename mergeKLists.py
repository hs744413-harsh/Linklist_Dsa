class Node:
  def __init__(self,val):
    self.val = val
    self.next = None
def conv(arr):
  head = Node(arr[0])
  temp = head
  for i in range(1,len(arr)):
    temp.next = Node(arr[i])
    temp = temp.next
  return head

  
def Print(head):
  curr = head
  while curr:
    print(curr.val , end=' --> ')
    curr = curr.next

def merge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    temp1 = head1
    temp2 = head2

    dummy = Node(-1)
    res = dummy

    while temp1 and temp2:
        if temp1.val < temp2.val:
            res.next = temp1
            temp1 = temp1.next
        else:
            res.next = temp2
            temp2 = temp2.next

        res = res.next

    res.next = temp1 if temp1 else temp2

    return dummy.next


def mergeKLists(lists):
    if not lists:
        return None

    if len(lists) == 1:
        return lists[0]

    first = lists[0]
    second = mergeKLists(lists[1:])

    return merge(first, second)


l1 = conv([1,3,5])
l2 = conv([1,2,4,7,8])
l3 = conv([1,6,9,10])
lists = [l1,l2,l3]

print("\n")
head = mergeKLists(lists)
Print(head)