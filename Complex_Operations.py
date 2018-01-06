import sys
def main():
    arg=[0,0,0,0]
    try:
        arg[0]=sys.argv[1]
    except IndexError:
        print "Provide Command line arguments"
        return
    try:
        arg[1]=sys.argv[2]
    except IndexError:
        print "Provide Command line arguments"
        return
    try:
        arg[2]=sys.argv[3]
    except IndexError:
        print "Provide Command line arguments"
        return
    try:
        arg[3]=sys.argv[4]
    except IndexError:
        print "Provide Command line arguments"
        return
    a=complex(int(arg[0]),int(arg[1]))
    b=complex(int(arg[2]),int(arg[3]))
    c=a+b
    print "\nAddition of the complex numbers give ",c
    c=a-b
    print "\nSubtraction of the complex numbers give ",c
    c=a*b 
    print "\nMultiplication of the complex numbers give ",c
    try:
        c=a/b
        print "\nDivision of the complex numbers give ",c
    except ZeroDivisionError:
        return
main()
