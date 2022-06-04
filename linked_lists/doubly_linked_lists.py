import gc

class LinkedListNode:
    def __init__(self, val):
        self.val=val
        self.prev=None
        self.next=None 

# Print all the nodes present in the linked list (n nodes)
# Time Complexity: O(n)
# Space Complexity: O(1)
def print_linked_list(head):
    temp=head
    while temp!=None:
        print(str(temp.val) + "->", end="")
        temp=temp.next
    print("None")
    return 

# Insert a new node at the beginning of the list
# Time Complexity: O(1)
# Space Complexity: O(1)
def insert_node_at_beginning(val, head):
    new_node=LinkedListNode(val)
    if head==None:
        head=new_node
    else:
        new_node.next=head
        head.prev=new_node
        head=new_node
    return head 

# Insert a new node at the end of the list (n nodes)
# Time Complexity: O(n)
# Space Complexity: O(1)
def insert_node_at_end(val, head):
    new_node=LinkedListNode(val)
    if head==None:
        head=new_node
    else:
        temp=head 
        while temp.next!=None:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
    return(head)

# Insert a new node after the node which has a specific value in the list (n nodes)
# Time Complexity: O(n)
# Space Complexity: O(1)
def insert_node(val, node_val, head):
    new_node=LinkedListNode(val)
    temp=head
    while(temp!=None and temp.val!=node_val):
        temp=temp.next
    if temp==None:
        return head 
    else:
        if temp.next:
            new_node.next = temp.next
            temp.next.prev = new_node
            new_node.prev=temp
            temp.next=new_node
        else:
            temp.next=new_node
            new_node.prev=temp
        return head

# Delete a linked list node from the beginning of the list
# Time Complexity: O(1)
# Space Complexity: O(1)
def delete_node_from_beginning(head):
    if head==None:
        return head 
    temp=head
    head=head.next 
    head.prev=None
    del temp 
    return head

# Delete a linked list node from the end of the list
# Time Complexity: O(n)
# Space Complexity: O(1)
def delete_node_from_end(head):
    if head==None:
        return head 
    else:
        temp=head
        while temp.next!=None:
            temp=temp.next 
      
    temp.prev.next=None
    temp.prev=None
    del temp
    return head

# Delete a linked list node with the value equals node_val
# Time Complexity: O(n)
# Space Complexity: O(1)
def delete_node(node_val, head):
    if head==None:
        return head
    temp=head 
    while temp!=None and temp.val!=node_val:
        temp=temp.next
    
    if temp.prev==None:
        temp.next.prev=None 
        head=temp.next 
        temp.next=None
    elif temp.next==None:
        temp.prev.next=None 
        temp.prev=None 
    else:
        temp.prev.next=temp.next
        temp.next.prev=temp.prev
    del temp 
    return head 

list_node_head=insert_node_at_beginning(10, None)
list_node_head=insert_node_at_beginning(11, list_node_head)
list_node_head=insert_node_at_end(13, list_node_head)
list_node_head=insert_node_at_end(19, list_node_head)
print_linked_list(list_node_head)
list_node_head=insert_node(17, 13, list_node_head)
print_linked_list(list_node_head)

list_node_head=delete_node_from_beginning(list_node_head)
list_node_head=delete_node_from_end(list_node_head)
list_node_head=delete_node(13, list_node_head)
print_linked_list(list_node_head)

gc.collect()