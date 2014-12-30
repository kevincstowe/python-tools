import sys
import getopt

#Main method as suggested by van Rossum, simplified
def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        opts, args = getopt.getopt(argv[1:], "h", ["help"])
        #Functional code goes here

    except:
        print "Error in args : " + str(argv[1:])
        return 2

if __name__ == "__main__":
    sys.exit(main())
