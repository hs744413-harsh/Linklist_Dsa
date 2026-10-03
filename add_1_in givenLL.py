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

def add_one(head):
  if head is None:
    return Node(1)
  new_head = reverse(head)
  temp = new_head
  carry = 1
  while temp:
    num = temp.val + carry
    carry = num//10
    temp.val = num%10
    temp = temp.next
  if carry:
    new = Node(carry)
    new.next = reverse(new_head)
    return new
  head = reverse(new_head)
  return head

# RECURSIVE METHOD OR BACKTRACKING>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>-_-?
def addCarry(head):
  if head is None:
    return 1
  num = head.val + addCarry(head.next)

  head.val = num%10
  carry = num//10
  return carry
  
def addOne(head):
  if head is None:
    return Node(1)
  carry = addCarry(head)

  if carry:
    new_head = Node(carry)
    new_head.next = head
    return new_head

  return head

arr = [1,2,2,2,2,9]
head = conv(arr)
Print(head)
print("\n")
head2 = addOne(head)
Print(head2)

      
  


