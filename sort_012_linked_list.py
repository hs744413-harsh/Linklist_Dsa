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
def sort_of_012(head):
  cnt0 = 0
  cnt1 = 0
  cnt2 = 0
  temp = head
  while temp:
    if temp.data == 0:
      cnt0 +=1
    elif temp.data == 1:
      cnt1+=1
    else:
      cnt2+=1
    temp = temp.next
  temp = head
  while temp:
    if cnt0:
      temp.data = 0
      cnt0-=1
    elif cnt1:
      temp.data = 1
      cnt1-=1
    else:
      temp.data = 2
      cnt2-=1
    temp = temp.next
  return head
def opt_sort_of_012(head):
  temp = head
  zero_head = Node(-1)
  one_head = Node(-1)
  two_head = Node(-1)
  zero = zero_head
  one = one_head
  two = two_head
  while temp:
    if temp.data == 0:
      zero.next = temp
      zero = temp
    elif temp.data == 1:
      one.next = temp
      one = temp
    else:
      two.next = temp
      two = temp
    temp = temp.next
  zero.next =one_head.next
  one.next = two_head.next
  two.next = None
  return zero_head.next
arr = [2,1,2,2,1,0,1,0]
head = conv(arr)
Print(head)
print("\n")
head1 = sort_of_012(head)
Print(head1)
print("\n")
head2 = opt_sort_of_012(head)
Print(head2)