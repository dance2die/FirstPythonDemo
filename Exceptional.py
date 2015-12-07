from pprint import pprint as pp
import sys


class CustomValueError(ValueError):
    def __init__(self, arg):
        self.error = arg
        self.args = {arg}



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


def testCustomValuError():
    try:
        raise CustomValueError("Value must be between 1 and 10.")
    except (CustomValueError) as e:
        print("Customer Value Error Exception!", e.error)

pp(convert(33))
# pp(convert("abc"))

try:
    raiseError()
except (ValueError) as e:
    pp(e)


testCustomValuError()

