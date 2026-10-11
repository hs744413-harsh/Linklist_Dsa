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

def reverse(head):
  curr = head
  prev = None
  while curr:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
  return prev
  
def find_kth(head,k):
  k -= 1
  while head and k > 0:
    k-=1
    head = head.next
  return head
  
def rev_K(head,k):
  if head is None or k <= 1:
    return head
    
  temp = head
  prev = None
  
  while temp:
    kth = find_kth(temp,k)
    
    if kth == None:
      if prev:
        prev.next = temp
      break
      
    next = kth.next
    kth.next = None
    
    kth = reverse(temp)
    
    if temp == head:
      head = kth
    else:
      prev.next = kth
    prev = temp
    temp = next
    
  return head

arr = [1,2,3,4,5]
head = conv(arr)
Print(head)
print("\n")
head2 = rev_K(head,2)
Print(head2)

