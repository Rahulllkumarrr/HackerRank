#!/bin/python3
###### Pre-written code Block ######

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

    def __repr__(self):
        return f"{self.data}->"


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        string = ""
        curr = self.head
        while curr.next:
            string += f"{curr.data} => "
            curr = curr.next
        string += f"{curr.data}"
        return string

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep):
    string = ""
    while node:
        string += str(node.data)

        node = node.next

        if node:
            string += sep

    print(string) 

##############################################
# TOD0: Add Reverse Functionality here

def reverse(llist):
    if not llist or not llist.next:
        return llist
    head = reverse(llist.next)
    headNext = llist.next
    headNext.next = llist
    llist.next = None
    return head

##############################################

if __name__ == "__main__":
    tests = 1
    llist_inputs = [5, 10, 4]
    for tests_itr in range(tests):
        llist_count = 3

        llist = SinglyLinkedList()

        for i in range(llist_count):
            llist_item = llist_inputs[i]
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1, " --> ")
        
##############################################