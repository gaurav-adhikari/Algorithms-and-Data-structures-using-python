# This program implements different summation functions and gives us the running times

# There are difference approaches to solve a common problem. Lets start with a summation problem

import time

# Approach 1
def addNumbersTillN1(n):
    tic=time.time()

    mySum=0
    for i in range(1,n+1):
        mySum=mySum+i

    toc=time.time()
    
    return mySum,(toc-tic)*1000


# Approach 2 

def addNumbersTillN2(n):
    
    tic=time.time()

    finalNumber = n*(n+1)/2

    toc=time.time()

    return finalNumber,(toc-tic)*1000





# Getting the average time taken


# Calling first approach
for i in range(5):
    print("Sum is %d and it took %f seconds"%addNumbersTillN1(10000))


print("\n\n")


# Calling second approach
for i in range(5):
    print("sum is %d and it took %10f seconds"%addNumbersTillN2(10000))



'''
 Conclusion -> Different runtimes can experienced as per the hardware configurations and the current system load.
            -> on my machine the approach 2 was about 100-200 times faster
            -> This signifies that we can levarage our hardware efficiently with efficient algorithms
'''