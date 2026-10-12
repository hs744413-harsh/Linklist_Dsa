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

def rotate_ll_by_K(head,k):
  if head is None or k == 0:
    return head
  cnt = 0
  temp = head
  tail = None
  while temp:
    cnt+=1
    if temp.next is None:
      tail = temp
    temp = temp.next

  k%=cnt

  while k>0:
    temp = head
    while temp.next != tail:
      temp = temp.next
    tail.next = head
    head = tail
    tail = temp
    tail.next = None
    k-=1

  return head

def opti_K_rot(head,k):
  if head is None or k == 0:
    return head
  cnt = 0
  temp = head
  tail = None
  while temp:
    cnt+=1
    if temp.next is None:
      tail = temp
    temp = temp.next

  k%=cnt

  if k == 0:
    return head

  steps = cnt - k
#   5 - 2 = 3

  new_tail = head
  for _ in range(steps-1):
    new_tail = new_tail.next

  tail.next = head
  head = new_tail.next
  new_tail.next = None
  

  return head

arr = [1,2,3,4,5]
head = conv(arr)
Print(head)
print("\n")
head2 = opti_K_rot(head,7)
Print(head2)
  