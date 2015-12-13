from pprint import pprint as pp

def test1():
    nums = [x for x in range(0,3)]
    i = iter(nums)
    pp(next(i))
    pp(next(i))
    pp(next(i))


def test2():
    words = "This is not a good test sentence".split()
    wordCounts = [len(word) for word in words]
    pp(wordCounts)


def main():
    # test1()
    test2()


if __name__ == "__main__":
    main()




