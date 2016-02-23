import sys
import getopt
import os

def get_size(start_path = '.', minsize=0):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.exists(fp):
                total_size += os.path.getsize(fp)
    if (total_size*1./1000000) > minsize:
        return str(total_size*1./1000000) + " MB"
    else:
        return None


#Main method as suggested by van Rossum, simplified
def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        opts, args = getopt.getopt(argv[1:], "hm:", ["help", "minsize="])

    except:
        print "Error in args : " + str(argv[1:])
        return 2

    minsize = 0

    for o, a in opts:
        if o in ["-m", "--minsize"]:
            minsize = int(a)

    if len(args) > 0:
        for arg in args:         
            size = get_size(arg, minsize)
            if size:
                print arg + " : " + size
    else:
        print "No arg, defaulting to local directory"
        size = get_size(".", minsize)
        print "./ : " + size
if __name__ == "__main__":
    sys.exit(main())
