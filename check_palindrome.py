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
    
def check_palindrome(head):
  if head is None or head.next is None:
    return True
  stack = []

  temp = head
  while temp:
    stack.append(temp.data)
    temp = temp.next

  temp = head
  while temp:
    if temp.data != stack[-1]:
      return False
    stack.pop()
    temp = temp.next
  return True

def reverse_recurion(head):
  if head is None or head.next is None:
    return head

  new_head = reverse_recurion(head.next)
  front = head.next
  front.next = head
  head.next = None
  return new_head

def reverse_it(head):
  if head is None or head.next is None:
    return head
  prev = None
  curr = head
  while curr:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
  return prev
  
def opti_check_palindrome(head):
  if head is None or head.next is None:
    return True
  slow = head
  fast = head
  while fast.next != None and fast.next.next != None:
    slow = slow.next
    fast = fast.next.next
  new_head = reverse_it(slow.next)
  first = head
  second = new_head
  while second:
    if first.data != second.data:
      reverse_it(new_head)
      return False
    first = first.next
    second = second.next
  reverse_it(new_head)
  return True

arr = [0,1,2,3,4,3,2,1,0]
head = conv(arr)
Print(head)
print("\n")
ans = opti_check_palindrome(head)
print(ans)
  