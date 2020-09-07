# data sturctures

# binary search tree

# example
#       1
#      / \
#     2    3
#    / \  / \
#   4  5  6  7

# Traverse the tree in two ways
#DFS - dept first search = contain = preorder , inorder , postorder
#BFS - birth first search = contain = level-order traversal

#preorder = root , left , right
#postorder = left , right , root
#inorder = left , root , right


class Node:

    def __init__(self , data = None):
        self.data = data
        self.left_child = None
        self.right_child = None

class Tree:

    def __init__(self):
            self.root = None


    #function to add element in the tree
    def add_node(self, element):
        if self.root == None:
            self.root = Node(element)
        else:
            self._add_node(self.root, element)

    ################################ DFS(depth first search) #################################

    #############   PREORDER TRAVERSAL  root , left , right

    def Preorder_Traversal(self):

        if self.root == None:
            print("Tree is empty")
        else:
            self._preorder(self.root)

    def _preorder(self , current):

        if current :
            print(current.data , end=" ")
            self._preorder(current.left_child)
            self._preorder(current.right_child)

    ############   POSTORDER TRAVERSAL  left , right , root

    def Postorder_Traversal(self):

        if self.root == None:
            print("Tree is empty ....")
        else:
            self._postorder(self.root)

    def _postorder(self , current):

        if current:
            self._postorder(current.left_child)
            self._postorder(current.right_child)
            print(current.data , end=" ")

    #############  INORDER TRAVERSAL left  , root , right

    def Inorder_Traversal(self):

        if self.root == None:
            print("Tree is empty ...")
        else:
            self._inorder(self.root)

    def _inorder(self , current):

        if current:
            self._postorder(current.left_child)
            print(current.data , end=" ")
            self._postorder(current.right_child)


    # function to display the tree or Level_ordertransversal of birth first search

    def Level_order_transversal(self):

        if self.root == None:
            print("Tree is empty ...")

        else:
            self._level_order_transversal(self.root)

    def _level_order_transversal(self, current):


        # making queue to add element of trees in it
        queue = []
        # adding the root node to the queue
        queue.append(current)
        #looping till the lenght of queue is above zero
        while len(queue) > 0:
            #then pop the first element in the queue and store it in node1
            node1 = queue.pop(0)
            #print the data in node1
            print(node1.data , end  = " ")
            # checking the left and right child of the node1 element if present  append it to the queue
            if (node1.left_child is not None) :
                queue.append(node1.left_child)

            if (node1.right_child is not None):
                queue.append(node1.right_child)


    def _add_node(self , current , val):

        if (current.data > val):

            if (current.left_child == None):
                current.left_child = Node(val)
            else:
                self._add_node(current.left_child, val)

        elif (current.data < val):

            if (current.right_child == None):
                current.right_child = Node(val)
            else:
                self._add_node(current.right_child, val)

        else:
            print('Value is Already Added in The tree..')


    # function to count the no. of Nodes in the tree

    def count(self):
        # making queue to add element of trees in it
        queue = []
        #make variable count
        count = 0
        # adding the root node to the queue
        queue.append(self.root)
        # looping till the lenght of queue is above zero
        while len(queue) > 0:
            # then pop the first element in the queue and store it in node1
            node1 = queue.pop(0)
            # Incrementing the count variable
            count += 1
            # checking the left and right child of the node1 element if present  append it to the queue
            if (node1.left_child is not None):
                queue.append(node1.left_child)

            if (node1.right_child is not None):
                queue.append(node1.right_child)
        print("No. of nodes in the tree is : ",count)

    #function to count minimum no.  in the tree

    def minimum_no_tree(self):

        current = self.root
        while (current.left_child is not None):
            current = current.left_child
        print("The minimum element in the tree is :",current.data)

    #function to find maximum no. of Nodes in the tree
    def maximum_no_tree(self):

        current = self.root
        while (current.right_child is not None):
            current = current.right_child
        print("The maximum element in the tree is :",current.data)


if __name__ == '__main__':
    tree = Tree()
    print("Elements present in Tree")
    tree.add_node(10)
    tree.add_node(20)
    tree.add_node(30)
    tree.add_node(40)
    tree.add_node(50)
    tree.Level_order_transversal()
    print()
    print("Preorder Traversal tree")
    tree.Preorder_Traversal()
    print()
    print("Postorder Traversal tree")
    tree.Postorder_Traversal()
    print()
    print("Inorder Traversal")
    tree.Inorder_Traversal()