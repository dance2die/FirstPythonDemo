from pprint import pprint as pp


class MyClass:
    MyVar = 0


def main():
    instance = MyClass()
    pp(instance.MyVar)
    pp(instance.__class__)


if __name__ == '__main__':
    main()


