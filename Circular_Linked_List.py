# data sturctures

# circular linked list - the last of the node will connect to the first node

class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
class Circular_Linked_list:
    def __init__(self):
        self.head = None
    # function to push element at the begnning
    def push_at_first(self , element):
        new_node = Node(element)
        new_node.next = self.head
        print("Element added in the list is :" , element)
        self.head = new_node


    # function to display it
    def display(self):
        temp = self.head
        print("Elements in the Circular Linked List")
        while temp :
            print(temp.data)
            temp = temp.next
            if temp == self.head:
                break



#main part of the program / calling part of the program

c  = Circular_Linked_list()

c.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

c.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

c.push_at_first(5)
c.display()

