from pprint import pprint as pp
import sys


def convert(value):
    try:
        return int(value)
    # except:
    #     pass
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
        return -1

def raiseError():
    raise ValueError


pp(convert(33))
# pp(convert("abc"))

try:
    raiseError()
except (ValueError) as e:
    pp(e)




