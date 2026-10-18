class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.child = None


def conv(arr):
    if not arr:
        return None

    head = Node(arr[0])
    temp = head

    for val in arr[1:]:
        temp.next = Node(val)
        temp = temp.next

    return head


def printLL(head):
    # Print main next chain
    temp = head
    nodes = []

    while temp:
        nodes.append(temp)
        temp = temp.next

    print(" -> ".join(str(node.val) for node in nodes))

    # Print child chains below their parent nodes
    child_nodes = [(i, node.child) for i, node in enumerate(nodes) if node.child]

    if not child_nodes:
        return

    width = len(" -> ".join(str(node.val) for node in nodes))
    line = [" "] * width

    for i, child in child_nodes:
        pos = sum(len(str(nodes[j].val)) + 4 for j in range(i))
        line[pos] = "|"

    print("".join(line).rstrip())

    line = [" "] * width

    for i, child in child_nodes:
        pos = sum(len(str(nodes[j].val)) + 4 for j in range(i))
        line[pos] = "v"

    print("".join(line).rstrip())

    # Print child chains
    output = [" "] * width

    for i, child in child_nodes:
        pos = sum(len(str(nodes[j].val)) + 4 for j in range(i))
        chain = []
        while child:
            chain.append(str(child.val))
            child = child.next

        text = " -> ".join(chain)
        for j, ch in enumerate(text):
            if pos + j < width:
                output[pos + j] = ch

    print("".join(output).rstrip())

def print_flat(head):
    while head:
        print(head.val, end=" -> ")
        head = head.child
    print("None")


def merge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    t1, t2 = head1, head2
    dummy = Node(-1)
    temp = dummy

    while t1 and t2:
        if t1.val < t2.val:
            temp.child = t1
            t1 = t1.child
        else:
            temp.child = t2
            t2 = t2.child

        temp = temp.child
        temp.next = None

    if t1:
        temp.child = t1
    else:
        temp.child = t2

    return dummy.child


def flatter(head):
    if head is None or head.next is None:
        return head

    head.next = flatter(head.next)
    head = merge(head, head.next)

    return head

head = conv([3,2,1,4,5])
head.next.child = conv([10])
head.next.next.next.child = conv([9]) 
head.next.next.next.next.child = conv([6,8]) 

printLL(head)
print("\n")
print("\n")
head1 = flatter(head)
print_flat(head1)