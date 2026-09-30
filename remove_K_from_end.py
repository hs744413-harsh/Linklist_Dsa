class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
def conv(arr):
  head = Node(arr[0])
  temp = head
  for i in range(1,len(arr)):
    temp.next = Node(arr[i])
    temp = temp.next
  return head
def Print(head):
  temp = head
  while temp:
    print(temp.data, end=" --> ")
    temp = temp.next
def remove_K_from_end(head,k):
  if head is None:
    return head
  temp = head
  n = 0
  while temp:
    n+=1
    temp = temp.next
  print(n)
  n-=k
  print(n)
  temp = head
  if n == 0:
    return head.next
  while temp:
    if n == 1:
      front = temp.next
      temp.next = front.next
      front.next = None
      break
    n-=1
    print(n)
    temp=temp.next
  return head
def opti_remove_K_from_end(head,k):
  dummy = Node(0)
  dummy.next = head

  fast = dummy
  for _ in range(k):
    fast = fast.next

  slow = dummy

  while fast.next != None:
    slow = slow.next
    fast = fast.next
    
  slow.next = slow.next.next

  return dummy.next

arr = [1,2,3,4,5,6,7,8]
head = conv(arr)
Print(head)
print("\n")
head1 = opti_remove_K_from_end(head,5)
Print(head1)
