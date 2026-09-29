class Node:
  def __init__(self,data):
    self.data = data
    self.prev = None
    self.next = None

def Print(head):
  curr = head
  while curr:
    print(curr.data, end=" <= => ")
    curr=curr.next

def del_head(head):
  if head is None and head.next is None:
    return None
  prev = head.next
  prev.prev = None
  head.next = None
  return prev

def del_tail(head):
  if head is None and head.next is None:
    return None
  temp = head
  while temp.next != None:
    temp = temp.next
  prev = temp.prev
  prev.next = None
  temp.prev = None
  return head

def del_K(head,k):
  if head is None and head.next is None:
    return None
  cnt = 0
  
  while temp:
    cnt+=1
    if cnt == k:
      break
    temp = temp.next
  
  front = temp.next
  back = temp.prev

  if front == None and back == None:
    return None
  elif front == None:
    back.next = None
    temp.prev = None
    return head
  elif back == None:
    front.prev = None
    temp.next = None
    return front
  else :
    back.next = front
    front.prev = back
    temp.next = None
    temp.prev = None
    return head

def conv(arr):
  head = Node(arr[0])
  prev = head
  for i in range(1, len(arr)):
    temp = Node(arr[i])
    temp.prev = prev
    prev.next = temp
    prev = temp
  return head

arr = [1,3,4,6,2,6]

head = conv(arr)
Print(head)
    