#!/usr/bin/env python3



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



def traversing(arr):
    for i in range(0,len(arr)-1):
        print("Element at index {} is {}".format(i,arr[i]))

def searching(element, arr):
    if element in arr:
        print("Found element {} at position {}".format(element,arr.index(element)))
    else:
        print("element not found")

def insertion(element, arr):
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

def deletion(element, arr, index):
    # Remove element by index
    arr.pop(index)
    print("New array after removing element from index {} is {}".format(index,arr))
    # Remove element 
    print("New array after removing element {} from arr is {}".format(element,arr))
    arr.remove(element)

def sorting(arr):
    print("sorted array is :", arr.sort())
    
def merging(arr1,arr2):
    print("New arr which is combination of {} and {} is :{}".format(arr1,arr2,arr1+arr2))

def main():
    arr = [1,2,3,4,5,6,7,8,9,10]
    traversing(arr)
    searching(9,arr)
    insertion(11,arr)
    deletion(11,arr,0)
    sorting(arr)
    arr2=[8,8,90,901]
    merging(arr,arr2)

main()
