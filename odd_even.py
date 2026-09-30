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

def odd_eve(head):
  temp = head
  dummy = Node(-1)
  res = dummy
  cnt = 0
  while temp:
    cnt+=1
    if cnt%2==1:
      var = Node(temp.data)
      res.next = var
      res = var
    temp = temp.next
  temp = head
  cnt = 0
  while temp:
    cnt+=1
    if cnt%2==0:
      var = Node(temp.data)
      res.next = var
      res = var
    temp = temp.next

  return dummy.next

def odd_eve_opti(head):
  odd = head
  even = head.next
  even_head = even

  while even != None and even.next != None:
    odd.next = odd.next.next
    even.next = even.next.next

    odd = odd.next
    even = even.next
  odd.next = even_head
  return head
  
arr1 = [1,2,3,4,5,6,7,8,9,0]
# arr2 = [4,3,2,1]

head1 = conv(arr1)
# head2 = conv(arr2)

Print(head1)
print("\n")
head2 = odd_eve(head1)
Print(head2)