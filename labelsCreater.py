# An python utility to create the labels.txt file for my tflite android application


def labelCreater(f):
    for x in range(65,91):
        f.write(chr(x)+"\n")


def main():
    f = open("/home/gaurav/Desktop/toco/labels.txt","w")
    labelCreater(f)


if __name__=="__main__":
    main()


'''
Conclusion
            -> Why not automate this boring step with a simple script
'''