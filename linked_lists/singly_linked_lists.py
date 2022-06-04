import gc

class LinkedListNode:
    def __init__(self, val):
        self.val=val
        self.next=None 

# Print all the nodes present in the linked list (n nodes)
# Time Complexity: O(n)
# Space Complexity: O(1)
def print_linked_list(head):
    temp=head
    while temp!=None:
        print(str(temp.val)+"->", end="")
        temp=temp.next
    print("None")

# Insert a new node at the beginning of the list
# Time Complexity: O(1)
# Space Complexity: O(1)
def insert_node_at_beginning(val, head):
    temp = LinkedListNode(val)
    if head == None:
        head=temp 
    else:
        temp.next=head 
        head=temp
    return head     

# Insert a new node at the end of the list (n nodes)
# Time Complexity: O(n)
# Space Complexity: O(1)
def insert_node_at_end(val, head):
    new_node = LinkedListNode(val)
    temp=head
    while temp.next!=None:
        temp=temp.next
    temp.next=new_node
    return head

# Insert a new node after the node which has a specific value in the list (n nodes)
# Time Complexity: O(n)
# Space Complexity: O(1)
def insert_node(val, head, node_val):
    new_node = LinkedListNode(val)
    temp=head 
    while temp.next!=None:
        if temp.val == node_val:
            break
        temp=temp.next
    
    new_node.next=temp.next 
    temp.next = new_node
    return head

# Delete a linked list node from the beginning of the list
# Time Complexity: O(1)
# Space Complexity: O(1)
def delete_node_from_beginning(head):
    head = head.next 
    return head 

# Delete a linked list node from the end of the list
# Time Complexity: O(n)
# Space Complexity: O(1)
def delete_node_from_end(head):
    prev = None 
    temp=head 
    while temp.next!=None:
        prev=temp 
        temp=temp.next 
    del temp 
    prev.next = None
    return head

# Delete a linked list node with the value equals node_val
# Time Complexity: O(n)
# Space Complexity: O(1)
def delete_node(node_val, head):
    prev=None
    temp=head 
    while(temp!=None and temp.val != node_val):
        prev=temp
        temp=temp.next 
    if temp==None:
        return head
    prev.next = temp.next 
    del temp 
    return head 

# Reverse the input linked list 
# Time Complexity: O(n)
# Space Complexity: O(1)
def reverse_linked_list(head):
    prev=None
    temp=head
    next=None

    while temp!=None:
        next=temp.next
        temp.next = prev
        prev=temp 
        temp=next 
    head=prev
    return head 

# Determine the index of the node with value equals node_val
# Time Complexity: O(n)
# Space Complexity: O(1)
def search_node(node_val, head):
    index=0
    temp=head 
    while(temp!=None and temp.val!=node_val):
        temp=temp.next 
        index+=1
    if temp!=None:
        return index
    return -1

# Update the value of node with value node_val to new value new_node_val
# Time Complexity: O(n)
# Space Complexity: O(1)
def update_node(node_val, new_node_val, head):
    temp=head 
    while(temp!=None and temp.val!=node_val):
        temp=temp.next

    if temp!=None:
        temp.val = new_node_val
        return 1
    return 0

# Two pointers concept to find the middle node in the linked list
# Time Complexity: O(n)
# Space Complexity: O(1)
def get_middle_node_approach1(head):
    slow=head
    fast=head 

    while slow!=None and fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next 
    return(slow.val)

# Traverse the list and count the nodes. Get the node at count/2 position to get the middle node.
# Time Complexity: O(n)
# Space Complexity: O(1)
def get_middle_node_approach2(head):
    temp=head
    counter=0

    while temp!=None:
        counter+=1
        temp=temp.next 
    
    mid = counter//2
    
    temp=head
    while mid>0:
        temp=temp.next
        mid-=1
    return(temp.val)

list_node_head = LinkedListNode(5)

list_node_head = insert_node_at_beginning(10, list_node_head)
list_node_head = insert_node_at_end(3, list_node_head)
list_node_head = insert_node_at_end(12, list_node_head)
list_node_head = insert_node_at_end(16, list_node_head)
list_node_head = insert_node(6, list_node_head, 5)
print("List after all the insertions: ")
print_linked_list(list_node_head)

list_node_head = delete_node_from_end(list_node_head)
list_node_head = delete_node(3, list_node_head)
print("List after all the deletions: ")
print_linked_list(list_node_head)

list_node_head = reverse_linked_list(list_node_head)
print_linked_list(list_node_head)

print("Node: "+str(3)+ " found at index:",search_node(3, list_node_head))
print(update_node(3, 14, list_node_head))

print("List middle node using approach 1: ")
get_middle_node_approach1(list_node_head)
print("List middle node using approach 2: ")
get_middle_node_approach2(list_node_head)

gc.collect()