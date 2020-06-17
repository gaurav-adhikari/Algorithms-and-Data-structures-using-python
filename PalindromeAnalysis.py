# Different approaches to a simple problem


# Approach1 The pythonista way 
def isPalindrome1(mystring):
    return  mystring==mystring[::-1]

# Approach2
def isPalindrome2(mystring):
    for i in range(0,int(len(mystring)/2)):
        if mystring[i]!=mystring[len(mystring)-i-1]:
            return False
        return True

# Approach3
def isPalindrome3(mystring):
    a=""
    for temp in mystring:
        a=temp+a
        if a==mystring:
            return True
    return False


def main():

    #Test Cases   

    assert isPalindrome1("radar")==True
    assert isPalindrome1("hello")==False

    assert isPalindrome2("radar")==True
    assert isPalindrome2("hello")==False


    assert isPalindrome3("radar")==True
    assert isPalindrome3("hello")==False
    
    pass

if __name__=="__main__":
    main()


'''
Conclusion
            -> Neat and clean code is so aesthetically pleasing to read

'''
