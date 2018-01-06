import sys
def main():
    a=12
    i=2
    while i <=a/2:
        if a%i==0:
            print "The given number ",a," is not prime"
            return
        else:
            i=i+1
    if i==a/2+1:
        print "The given number ",a," is prime"
main()
