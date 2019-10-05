#!/usr/bin/env python3

import numpy as np

class BasicArray:

    """
    append()    Adds an element at the end of the list
    clear() Removes all the elements from the list
    copy()  Returns a copy of the list
    count() Returns the number of elements with the specified value
    extend()    Add the elements of a list (or any iterable), to the end of the current list
    index() Returns the index of the first element with the specified value
    insert()    Adds an element at the specified position
    pop()   Removes the element at the specified position
    remove()    Removes the first item with the specified value
    reverse()   Reverses the order of the list
    sort()  Sorts the list
    """

    def traversing(self, arr):
        for i in range(0,len(arr)-1):
            print("Element at index {} is {}".format(i,arr[i]))

    def searching(self, element, arr):
        if element in arr:
            print("Found element {} at position {}".format(element,arr.index(element)))
        else:
            print("element not found")

    def insertion(self, element, arr):
        arr.append(element)
        print("New array is {}".format(arr))

        """
        Adding element at specific position will be as follow:
        ex: adding at position 2 element 'x'
        """
        tmp = []
        for i in range(0,len(arr)-1):
            if i == 2:
                tmp.append('x')
                tmp.append(arr[i])
            tmp.append(arr[i])
        # Note: if you copy array like arr=tmp, try it your self if you modify one if will modify another
        arr=tmp.copy()
        # clear variable
        tmp.clear()
        print("New array after adding 'x' as position 2 is:",arr)

    def deletion(self, element, arr, index):
        # Remove element by index
        arr.pop(index)
        print("New array after removing element from index {} is {}".format(index,arr))
        # Remove element 
        arr.remove(element)
        print("New array after removing element {} from arr is {}".format(element,arr))
    
    def sorting(self, arr):
        print("orignal arr",arr)
        arr.sort()
        print("sorted array of is :{}".format(arr))

    def merging(self, arr1, arr2):
        print("New arr which is combination of {} and {} is :{}".format(arr1,arr2,arr1+arr2))

    def main(self):
        arr = [1,2,3,4,5,6,7,8,9,10]
        self.traversing(arr)
        self.searching(9,arr)
        self.insertion(11,arr)
        self.deletion(11,arr,0)
        s_arr = [0,5,7,3,2,90,4,6,7]
        self.sorting(s_arr)
        arr2=[8,8,90,901]
        self.merging(arr,arr2)


class NumpyArray:
    def createarray(self):
        arr_1d = np.array([1,6,3,7,9,0])
        print("created array:", arr_1d)
        print("Type of array:", type(arr_1d))
        print("Size of array in each dimention:", arr_1d.shape)

        # create 2D array
        arr_2d = np.array([[1,2,4],[3,4,5]])
        print("created 2d numpy array:\n", arr_2d)
        print("Type of arr", type(arr_2d))
        # it will return len of each array if its same
        print("Size of arr", arr_2d.shape)

        # create diffrent type of multi-dimentional arrays
        ## by default numpy will create array of floats if not specified type by using `dtype`
        arr_zeros = np.zeros([2,3])
        print("Array of Zeros:\n", arr_zeros)
        arr_ones = np.ones([3,3])
        print("Array of ones:\n", arr_ones)
        arr_rand = np.random.random([3,2])
        print("Array of random:\n", arr_rand)
        array_int = np.random.randint(low=90,high=200, size=(3,3))
        print("Array of random number from range 90 to 200 and size 3x3:\n", array_int)
        arr_const = np.full([2,3],5)
        print("Array of constants:\n", arr_const)
        arr_indentity = np.eye(4, dtype=int)
        print("Indentuity matrix:\n", arr_indentity)

    def traversing(self, arr_1d, arr_2d):
        for e in arr_1d: print(e)

        # Create transpose of array
        print("Transponse of an array - array.T:\n", arr_2d.T)
        print("Original array:\n", arr_2d)

        # iterating through array
        for x in np.nditer(arr_2d, order = 'C'):
            print("element in array by column is:", x)

        # iterating through array row vise
        for x in np.nditer(arr_2d, order = 'F'):
            print("element in array by row is:", x)
    #def Searching
    #def Insertion
    #def Deletion
    #def Sorting
    #def Merging

    def main(self):
        self.createarray()
        a1=np.arange(0,20,2)
        a2=a1.reshape(2,5)
        self.traversing(a1,a2)
        #traversing()

if __name__ == "__main__":
    obj1 = BasicArray()
    obj1.main()

    print("\n\n=================== Using numpy ===================\n\n")
    obj2 = NumpyArray()
    obj2.main()
