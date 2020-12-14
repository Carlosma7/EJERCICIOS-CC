import etcd3
import sys

def main( argv = [] ):
	etcd = etcd3.client()
	if(argv):
		print(etcd.get(argv[0]))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1:])
    else:
        print("Wrong number of arguments")
