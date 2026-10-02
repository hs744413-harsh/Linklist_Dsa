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
def revrse_LL(head):
  curr = head
  prev = None

  while curr:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp
  return prev

def reverse_recurive(head):
  # base case
  if head is None or head.next is None:
    return head
  # recurion method
  new_head = reverse_recurive(head.next)
  front = head.next
  front.next = head
  head.next = None

  return new_head

arr = [2,1,2,3,4,5,6]
head = conv(arr)
Print(head)
print("\n")
head2 = reverse_recurive(head)
Print(head2)
  