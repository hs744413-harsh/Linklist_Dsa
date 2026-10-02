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

arr = [2,1,2,3,4,5,6]
head = conv(arr)
Print(head)
print("\n")
head2 = revrse_LL(head)
Print(head2)
  