class Node:
  def __init__(self,val):
    self.val = val
    self.next = None
def conv(arr):
  head = Node(arr[0])
  temp = head
  for i in range(1,len(arr)):
    var = Node(arr[i])
    temp.next = var
    temp = var
  return head
def Print(head):
  curr = head
  while curr:
    print(curr.val , end=' --> ')
    curr = curr.next
def middle(head):
  if head is None or head.next is None:
    return head
  slow = head
  fast = head.next
  while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next
  return slow.val

arr = [1,3,4,7,1,2]
head = conv(arr)
Print(head)
print("\n")
ans= middle(head)
print(ans)

      
  


