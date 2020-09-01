# data sturcture set


####################################    OPERATIONS ##################################


# function to tell that the set is empty or not
def is_empty(set):
    if set == ([]):
        print(True)
    else:
        print(False)


# function to add element in set
def add(set, element):
    set.add(element)
    return


# function to delete element in set
def delete(set, element):
    set.remove(element)
    return


# function to calculate lenght of the set
def lenght_set(set):
    print("Lenght of stack is ", len(set))


# function to search element in the stack
def search_element(set, element):
    if element not in set:
        print("Element not present")

    for i in set:
        if i == element:
            print("Element present")
            break


# function to display set
def display(set):
    print("Element present in the set : ", set)


if __name__ == '__main__':
    s = set([])

    # adding element
    add(s, 1)
    add(s, 2)
    add(s, 3)
    add(s, 4)
    add(s, 5)

    # removing element
    delete(s , 5)

    # lenght
    lenght_set(s)

    # display set
    display(s)

    # search element in set
    search_element(s, 5)

    is_empty(s)
