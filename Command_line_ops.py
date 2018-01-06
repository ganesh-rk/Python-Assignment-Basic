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
    a=arg[0]
    arg[0]+=arg[1]
    print "\n Addition of the two numbers gives ",arg[0]
    arg[0]=a
    arg[0]-=arg[1]
    print "\n Subtraction of the two numbers gives ",arg[0]
    arg[0]=a
    arg[0]*=arg[1]
    print "\n Multiplication of the two numbers gives ",arg[0]
    arg[0]=a
    arg[0]/=arg[1]
    print "\n Division of the two numbers gives ",arg[0]
    arg[0]=a
    arg[0]%=arg[1]
    print "\n Modulus of the two numbers gives ",arg[0]
    arg[0]=a
    arg[0]**=arg[1]
    print "\n Exponentiation of the two numbers gives ",arg[0]
    arg[0]=a
    arg[0]//=arg[1]
    print "\n Floor division of the two numbers gives ",arg[0]
main()
