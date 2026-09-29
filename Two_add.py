class Node:
  def __init__(self,data):
    self.data = data
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
    print(curr.data , end=' --> ')
    curr = curr.next

def add_two(head1,head2):
  temp1 = head1
  temp2 = head2

  dummy = Node(-1)
  curr = dummy

  carry = total = 0

  while temp1 or temp2 or carry:
    total = carry
    if temp1:
      total += temp1.data
      temp1 = temp1.next
    if temp2:
      total += temp2.data
      temp2 = temp2.next
    
    num = total%10
    carry = total // 10
    var = Node(num)
    curr.next = var
    curr = var

  return dummy.next


arr1 = [1,2,3,4]
arr2 = [4,3,2,1]

head1 = conv(arr1)
head2 = conv(arr2)

Print(head1)
print("\n")
Print(head2)
print("\n")
head3 = add_two(head1,head2)
Print(head3)