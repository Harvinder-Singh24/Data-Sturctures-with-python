# Data sturctures

# Queue

#######################  QUEUE FUNCTION  ######################

#function to check the queue is empty or not
def is_empty(queue):
    if queue == []:
        return True
    else:
        return False

#function to enqueue the data

def enqueue(queue , element):
    queue.append(element)
    if is_empty(queue):
        print( "The queue is empty")


# function to display the queue

def display(queue):
    a = []
    for i in queue:
        a.append(i)
    print("Element present in the queue is ",a)


Queue = []

enqueue(Queue , 0)
enqueue(Queue , 1)

display(Queue)