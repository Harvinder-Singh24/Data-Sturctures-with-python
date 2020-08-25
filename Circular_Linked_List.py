# data sturctures

# circular linked list - the last of the node will connect to the first node

class Node:
    def __init__(self , data):
        self.data = data
        self.next = None
class Circular_Linked_list:
    def __init__(self):
        self.head = None


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

c.head = Node(0)
second = Node(1)
third = Node(3)

c.head.next = second
second.next = third

c.display()

