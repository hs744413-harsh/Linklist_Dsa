class Node:
  def __init__(self,val):
    self.val = val
    self.next = None
    self.prev = None
def conv(arr):
  head = Node(arr[0])
  temp = head
  prev = head
  for i in range(1,len(arr)):
    var = Node(arr[i])
    temp.next = var
    var.prev = prev
    temp = var
    prev = var
  return head
def Print(head):
  curr = head
  while curr:
    print(curr.val , end=' <--> ')
    curr = curr.next

def pairs(head,target):
  if head is None or head.next is None:
    return []

  seen = []
  l = head
  r = head
  while r.next != None:
    r = r.next

  while l.val <= r.val:
    sum = l.val + r.val
    if sum == target:
      seen.append([l.val,r.val])
      l = l.next
      r = r.prev
    elif sum > target:
      r = r.prev
    else:
      l = l.next

  return seen

arr = [1,2,3,4,9]
head = conv(arr)
Print(head)
print("\n")
ans = pairs(head,5)
print(ans)

