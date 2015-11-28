from pprint import pprint as pp


def convert(value):
    converted = -1
    try:
        converted = int(value)
        pp("Conversion succeeded! converted = {}".format(converted))
    #except (ValueError, TypeError):
    except:
        pp("Conversion failed!")
    return converted


pp(convert(33))
pp(convert("abc"))
