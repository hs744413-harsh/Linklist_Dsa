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

def merge_LL(head1,head2):
  if head1 is None:
    return head2
  if head2 is None:
    return head1

  temp1 = head1
  temp2 = head2

  dummy = Node(-1)
  curr = dummy

  while temp1 != None and temp2 != None:
    if temp1.val < temp2.val:
      curr.next = temp1
      curr = temp1
      temp1 = temp1.next
    else:
      curr.next = temp2
      curr = temp2
      temp2 = temp2.next

  while temp1:
    curr.next = temp1
    curr = temp1
    temp1 = temp1.next
    
  while temp2:
    curr.next = temp2
    curr = temp2
    temp2 = temp2.next

  return dummy.next
  
arr1 = [2,4,8,10]
arr2 = [1,3,3,6,11,14]
head1 = conv(arr1)
head2 = conv(arr2)
Print(head1)
print("\n")
Print(head2)
print("\n")
head3 = merge_LL(head1,head2)
Print(head3)
  