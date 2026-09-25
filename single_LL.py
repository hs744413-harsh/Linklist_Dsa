class Node:
  def __init__(self,Data):
    self.data = Data
    self.next = None

def print_LL(head):
  while head:
    print(head.data, end=' ---> ')
    head = head.next

def convert_into_Arr(arr):
  if not arr:
    return None

  head = Node(arr[0])
  curr = head
  for i in range(1,len(arr)):
    curr.next = Node(arr[i])
    curr = curr.next

  return head

def del_front(head):
  if not head:
    return None
  return head.next

def del_back(head):
  if not head or head.next == None:
    return None
  curr = head
  while curr.next.next != None:
    curr = curr.next
  curr.next = None

  return head

def del_K(head,k):
  if not head:
    return head
  if k == 1:
    return head.next

  curr = head

  for i in range(k-2):
    curr = curr.next

  curr.next = curr.next.next

  return head

def del_el(head,k):
  if not head:
    return head
  if head.data == k:
    return head.next

  curr = head
  prev = None

  while curr.next != None:
    if curr.data == k:
      prev.next = prev.next.next
    prev = curr
    curr = curr.next

  return head
    



# *********************************************************************************

arr = [1,2,3,4,5,6,7,8,9]

head = convert_into_Arr(arr)
print_LL(head)
print("\n")
head = del_front(head)
print_LL(head)
head = del_back(head)
print("\n")
print_LL(head)
head = del_K(head,6)
print("\n")
print_LL(head)
print("\n")
head = del_el(head,2)
print_LL(head)
