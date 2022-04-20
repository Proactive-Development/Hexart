import sys
from modules import create_text
import random
if __name__ == "__main__":
    for i in sys.argv:
        if i == "-r":
            print(create_text.generate(str(random.randint(10000000000000000000,99999999999999999999)).encode('utf-8').hex()))
            sys.exit(0)
    print("HEXART 20 char")
    print(create_text.generate(str(sys.argv[-1].encode('utf-8').hex())))
    