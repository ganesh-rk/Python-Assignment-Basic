import sys

def main():
    try:
        arg1=sys.argv[1]
    except IndexError:
        print"Provide command  line arguments"
        return
    try:
        arg2=sys.argv[2]
    except IndexError:
        print"Provide command  line arguments"
        return
    try:
        arg3=sys.argv[3]
    except IndexError:
        print"Provide command  line arguments"
        return
    print "\nFirst number is ",arg1
    print "\nSecond number is ",arg2
    print "\nThird number is ",arg3
    print "\n The biggest of the three is ",max(arg1,arg2,arg3)    
main()
