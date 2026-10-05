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

def remove_duplicate(head):
  if head is None or head.next is None:
    return head
  temp = head
  while temp and temp.next != None:
    if temp.next.val == temp.val:
      curr = temp
      while curr and curr.val == temp.val:
        curr = curr.next
      if temp == head:
        head = curr
        temp = head
      else:
        prev = head
        while prev.next != temp:
          prev = prev.next
        prev.next = curr
        temp = prev
    else:
      temp = temp.next
  return head

def remove_duplicate_map(head):
  if head is None or head.next is None:
    return head
  seen = {}

  temp = head
  while temp:
    if temp.val in seen:
      seen[temp.val] +=1
    else:
      seen[temp.val] = 1
    temp = temp.next

  temp = head
  prev = None
  for key,value in seen.items(): 
      if seen[key] == 1:
        temp.val = key
        prev = temp
        temp = temp.next

  if prev is None:
    return None
  prev.next = None
  return head

def dummy_sol(head):
  if head is None or head.next is None:
    return head
    
  dummy = Node(-1)
  dummy.next = head
  
  curr = head
  prev = dummy
  
  while curr:
    val = curr.val
    if curr.next and val == curr.next.val:
      while curr and curr.val == val:
        curr = curr.next
      prev.next = curr
    else:
      prev = curr
      curr = curr.next
  return dummy.next

arr = [1,1,2,3,3,4,5,5,6]
head = conv(arr)
Print(head)
print("\n")
head1 = dummy_sol(head)
Print(head1)