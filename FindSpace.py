import sys
import getopt
import os

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return str(total_size*1./1000000) + " MB"

#Main method as suggested by van Rossum, simplified
def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        opts, args = getopt.getopt(argv[1:], "h", ["help"])

    except:
        print "Error in args : " + str(argv[1:])
        return 2

    if len(args) > 0:
        for arg in args:
            print arg + " : " + get_size(arg)
    else:
        print "Need at least one arg..."
        return 1

if __name__ == "__main__":
    sys.exit(main())
