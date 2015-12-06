import sys
from pprint import pprint as pp


f = open("./First.py", mode='rt', encoding='utf-8')


def main():
    for line in f.readlines():
        # pp(line)
        sys.stdout.write(line)

if __name__ == '__main__':
    main()


