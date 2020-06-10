# Analysis of swapping two variables in python


# Approach 1
def swap1(a,b):
    temp=a
    a=b
    b=temp
    return a,b

#Approach 2 (cleaner)
def swap2(a,b):
    a,b=b,a
    return a,b


def main():

    assert swap1(10,20) == (20,10)
    assert swap2(10,20) == (20,10)


if __name__=="__main__":
    main()

'''
 Conclusion
            -> Just two ways we can swap variables
            -> learnt about optimistic nihalism so kinda baffled by it for past couple of days.  
'''
