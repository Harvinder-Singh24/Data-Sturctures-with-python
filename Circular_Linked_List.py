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
    # to search an element present in linked list
    def search(self , element):

        temp = self.head
        position = 0
        while temp:
            position += 1
            if element == temp.data:
                print("Element found at index", position-1)
                break
            temp = temp.next
        else:
            print("Element not found")
    # to delete first element from the linked list

    def delete_first(self):

        current = self.head
        self.head = current.next
        current.next = None
        print("Element deleted from the linked list is " , current.data)

    # to delete the last node in circular linked list

    def delete_search(self , element):

        if element == self.head:
            current = self.head
            self.head = current.next
            current.next = None
        else:
            pass



    # to find the lenght of the linked list
    def lenght(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
            if temp == self.head:
                break
            print(count)


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


c.head.next = second
second.next = third
third.next = fourth


c.delete_search(1)
c.display()