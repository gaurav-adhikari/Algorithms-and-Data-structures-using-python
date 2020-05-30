# Implentation of Bubble sort in python


# complexity O(n^2)
def sort(mylist):

    for i in range(len(mylist)-1):

        # set range accordingly as numbers after ith indexes are already sorted
        for j in range(0, len(mylist)-i-1):

            # interchange their values
            if mylist[j] > mylist[j+1]:

                temp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1]=temp

            print(mylist)
    
    return mylist 


def main():

    a = [56, 74, 23, 48, 89, 5, 10]
    print("sorted list is \n", sort(a))

    pass

if __name__ == "__main__":
    main()



'''
 Conclusion
            -> Bubble sort took about 0.066 seconds to complete
            
'''