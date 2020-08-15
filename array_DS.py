# data sturcture
#full Array as ADT

class Array :
    # constructor of the array
    def __init__(self):
        self._thearray = list()
    # to add
    def add(self , element):
        return self._thearray.append(element)
    #to delete element from the user choice
    def del_element(self  , element):
        if element in self._thearray:
            for i in range(0,len(self._thearray)-1):
                if self._thearray[i] == element:
                    self._thearray.remove(element)
        else:
            print("Element is not present")

    #to display
    def display(self):
        print(self._thearray)
    # to reverse a array
    def reverse(self):
        return self._thearray[::-1]
    # to sort an array in ascending orders
    def asc_sorting(self):
        return self._thearray.sort()
    # ti sort array in desecnding order
    def desc_sorting(self):
        return self._thearray.sort(reverse=True)
    # search using binary search allgorithm
    
arr = Array()
#adding
arr.add(23)
arr.add(20)
arr.add(30)
arr.add(45)


arr.del_element(45)

arr.display()
