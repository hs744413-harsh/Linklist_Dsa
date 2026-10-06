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

def reverse(left,right):
  curr = left
  prev = None

  while curr != right:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
  return prev

def reverse_left_to_right(head,L,R):
  if head is None or head.next is None:
    return head

  temp = head
  cnt = 0
  left = None
  prev = temp
  right = None
  while temp:
    cnt+=1
    if cnt==L-1:
      prev = temp
      left = temp.next
      
    if cnt==R:
      right = temp.next
      break
    temp = temp.next
  prev.next = reverse(left,right)
  left.next = right

  return head

def Optim(head,l,r):
  if head is None or l == r:
    return head

  dummy = Node(0)
  dummy.next = head

  prev = dummy

  for _ in range(l-1):
    prev = prev.next
  curr = prev.next
  left = curr
  before = prev
  for _ in range(r-l+1):
    temp = curr.next
    curr.next = before
    before = curr
    curr = temp

  #  RECONNECT
  prev.next = before
  left.next = curr

  return head
      

arr = [1,2,3,4,5,6,7]
head = conv(arr)
Print(head)
print("\n")
head1 = Optim(head,2,5)
Print(head1)