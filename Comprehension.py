from pprint import pprint as pp

def test1():
    nums = [x for x in range(0,3)]
    i = iter(nums)
    pp(next(i))
    pp(next(i))
    pp(next(i))


def main():
    test1()


if __name__ == "__main__":
    main()




