# Implentation of Bubble sort in python


# complexity O(n^2)
def bubbleSort(mylist):

    for i in range(len(mylist)-1):

        # set range accordingly as numbers after ith indexes are already sorted
        for j in range(0, len(mylist)-i-1):

            # interchange their values
            if mylist[j] > mylist[j+1]:

                temp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = temp

    return mylist

# Complexity O(nlog(n))
def mergeSort(mylist):

    length = len(mylist)

    if length > 1:

        # Divide the list and separate the list
        mid = length//2
        l = mylist[:mid]
        r = mylist[mid:]

        mergeSort(l)
        mergeSort(r)

        i = j = k = 0
        while i < len(l) and j < len(r):

            if l[i] < r[j]:
                mylist[k] = l[i]
                i += 1
            else:
                mylist[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            mylist[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            mylist[k] = r[j]
            j += 1
            k += 1

    return mylist

# complexity O(n^2)
def selectionSort(myarray):

    for i in range(len(myarray)):

        minInd = i
        for j in range(i+1, len(myarray)):

            if myarray[j] < myarray[i]:
                minInd = i

        # Interchaning variables
        temp = myarray[i]
        myarray[i] = myarray[minInd]
        myarray[minInd] = temp

    return myarray


def main():

    a = [56, 74, 23, 48, 89, 5, 10, 1]

    assert bubbleSort(a) == [1, 5, 10, 23, 48, 56, 74, 89]

    assert mergeSort(a) == [1, 5, 10, 23, 48, 56, 74, 89]

    assert selectionSort(a) == [1, 5, 10, 23, 48, 56, 74, 89]

    pass


if __name__ == "__main__":
    main()

'''
 Conclusion
            -> Bubble sort took about 0.066 seconds to complete
            -> Merge sort took about approx half the time as that of Bubble sort
            -> Divide and conquer solves a lot boiler-plate code 
            -> Selection sort has the O(n^2) and is not the sorting algorithm of my choice.  
'''
