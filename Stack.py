# data sturcture
#stack

def is_empty(stack):
    if stack == []:
        print("It is empty")


def push(stack , element):
    stack.append(element)

def pull(stack):
    a = stack.pop()
    print("Element pop is " ,a )

def peak(stack) :
    s = stack[0]
    print("THe top element in the stack is" , s)

def search_element(stack ,element):
    is_empty(stack)
    positon = 0
    if element == stack[0]:
        print("Element found at index" , positon)
    else:
        for i in range(1, len(stack)):
            positon += 1
            if element == stack[i]:
                print("Element found at the index ", positon)
                break
            else:
                print("Element not found")
                break




def display(stack):
    print("Element in the stack ",stack)


stack  = []
push(stack , 3)
push(stack , 1)
push(stack , 2)
search_element(stack , 4)

display(stack)
