import sys

def main():
    arg =[0,0]
    try:
        arg[0]=int(sys.argv[1])
    except IndexError:
        print "Provide Command Line arguments"
        return
    try:
        arg[1]=int(sys.argv[2])
    except IndexError:
        print "Provide Command Line arguments"
        return
    a=(arg[0] and arg[1])
    b=(arg[0] or arg[1])
    c=not (arg[0] and arg[1])
    print "\nAnd operation between the two numbers give ",a
    print "\nOr operation between the two numbers give ",b
    print "\nNand operation between the two numbers give ",c
main()
    
