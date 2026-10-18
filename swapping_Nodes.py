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

def swapNodes(head,k):
  if head is None or head.next is None:
    return head

  cnt = 0
  temp = head
  while temp:
    cnt+=1
    temp = temp.next

  if k > cnt:
    return head
    
  print(temp)
  steps = cnt - k
  print(steps," ",cnt, " ", k)

  first = head
  second = head

  for _ in range(k-1):
    first = first.next
    
  for _ in range(steps):
    second = second.next
    

  first.val, second.val = second.val , first.val
    

  return head
  

head = conv([1,2,3,4,5,6,7,8,9])

Print(head)
print("\n")
head1 = swapNodes(head,5)

Print(head1)